"""
File/stream related tools.
"""
import io
import os
import tempfile
import typing
import urllib.request

from dslibrary.engine_intf import FileSystemLocal, FileSystemReadOnly, S3Connection

try:
    import fsspec
except ImportError:
    fsspec = None


class FileOpener(object):
    """
    Opens read/write streams on a wide range of URIs.
    """
    def __init__(self, root_folder: str=None):
        """
        :param root_folder:   Default folder, in case relative local paths are given.
        """
        self._root = os.path.expanduser(root_folder or ".")

    def http_open(self, path: str, mode: str, **kwargs):
        """
        HTTP and FTP can be handled with the built-in urllib.

        :param path:        URI specifying an HTTP or FTP location.
        :param mode:        'r' and 'rb' are supported.
        :param kwargs:      'headers' can be specified.
        :return:        A stream, if the supplied arguments were supported, or None.
        """
        if path.startswith("https://") or path.startswith("http://") or path.startswith("ftp://"):
            if "?" in mode:
                if "w" in mode:
                    return True
                try:
                    # TODO a HEAD would be better to check existence than starting a full transfer and abandoning it
                    strm = self.http_open(path, mode.replace("?", ""), **kwargs)
                    strm.close()
                    return True
                except:
                    return False
            allowed = ("data", "timeout", "cafile", "cadefault", "context")
            use_kwargs = {k: v for k, v in kwargs.items() if k in allowed}
            if mode == "rb":
                request = urllib.request.Request(url=path, headers=kwargs.get("headers") or {})
                return urllib.request.urlopen(request, **use_kwargs)
            if mode == "r":
                byte_stream = self.http_open(path, mode, **kwargs)
                return io.TextIOWrapper(byte_stream)
            if mode in ("w", "wb"):
                # data can be sent to a REST service
                #  - set method to POST or PUT
                #  - set any needed authentication headers in 'headers'
                #  - path is URL plus any required arguments in the query string
                request = urllib.request.Request(url=path, headers=kwargs.get("headers") or {}, method=kwargs.get("method", "POST"))
                if "data" in use_kwargs:
                    use_kwargs.pop("data")
                return write_stream_with_read_on_close(mode, r_mode='rb', on_close=lambda stream: urllib.request.urlopen(request, data=stream, **use_kwargs))
            raise ValueError(f"Mode is not supported for {path}: {mode}")

    def uri_open(self, path: str, mode: str, **kwargs):
        """
        Open specific/exotic URIs, like s3, abfs, adl, gs, etc..

        :param path:        The URI, usually of the form PROTO://BUCKET/PATH.
        :param mode:        'r', rb', 'w', etc.
        :param kwargs:      Additional options passed through to the target library (i.e. fsspec).
        :return:        A file stream, if a handler was found.
        """
        if "://" not in path:
            return
        if not fsspec:
            raise ImportWarning(f"The 'fsspec' package is required to open {path}")
        kwargs = adapt_fsspec_storage_options(kwargs)
        if "storage_options" in kwargs:
            kwargs = kwargs["storage_options"]
        if path.startswith("s3:") and mode and "a" in mode:
            raise ValueError(f"Append mode is not supported for {path}")
        if "?" in mode:
            if "w" in mode:
                return True
            fss = connect_to_filesystem(path, **kwargs)
            return fss.exists(path)
        return fsspec.open(path, mode=mode, **kwargs)

    def local_open(self, path: str, mode: str, **kwargs):
        """
        Open local files.
        :param path:    A relative path, relative to self._root, or an absolute path.
        :param mode:    'r', 'rb', 'w', 'wb', 'a', 'ab'.
        :param kwargs:  No additional options are recognized.
        :return:    A file stream.
        """
        full_path = os.path.join(self._root, path)
        if "?" in mode:
            if "w" in mode:
                folder = os.path.split(full_path)[0]
                return os.path.exists(folder or ".")
            return os.path.exists(full_path)
        return open(full_path, mode)

    def open(self, path: str, mode: str, **kwargs):
        """
        Open files.

        :param path:    Path to file, or URI of file.
        :param mode:    Open mode (r, rb, w, wb, a, ab)
        :param kwargs:  Additional arguments to customize details of the operation.
        :return:    File-like object.
        """
        # some really simple external file access can be handled without fsspec
        stream = self.http_open(path, mode, **kwargs)
        if stream is not None:
            return stream
        # URIs go through fsspec
        stream = self.uri_open(path, mode, **kwargs)
        if stream is not None:
            return stream
        # local files
        if ":" in path:
            raise ValueError(f"Unsupported URL: {path}")
        return self.local_open(path, mode, **kwargs)


def write_stream_with_read_on_close(w_mode: str, r_mode: str, on_close: typing.Callable):
    """
    Open a write stream that saves data in a temporary file and sends a read stream for that data to a supplied method.
    :param w_mode:          'w' or 'wb'.
    :param r_mode:          'r' or 'rb'.
    :param on_close:        Method called with read stream
    :return:
    """
    fh = tempfile.NamedTemporaryFile(mode=w_mode, delete=False)
    def closer():
        if not fh.closed:
            fh.flush()
        with open(fh.name, r_mode) as f_r:
            on_close(f_r)
        os.remove(fh.name)
    fh.close = closer
    return fh


def connect_to_filesystem(uri: str, for_write: bool=False, **kwargs):
    """
    Generate an open(filename, mode) method based on a URI and credentials.
    :param uri:             A partial URI like "s3://bucket", or a local path.
    :param for_write:       Whether to allow write access.
    :param kwargs:          Additional arguments, namely credentials.
    :return:            A FileSystem instance that lets you work with files in the remote filesystem.
    """
    if "://" not in uri:
        # uri can just be a local path
        fs = FileSystemLocal(uri)
    else:
        # otherwise we assume the usual cloud format: protocol://bucket
        protocol, bucket = uri.strip("/").split("://", maxsplit=1)
        bucket = bucket.split("/")[0]
        if ":" in bucket:
            raise ValueError(f"Invalid URI for external filesystem: {uri}")
        if protocol == "s3":
            # fsspec does not support streaming upload or 'read_only' mode, so we have our own implementation
            return S3Connection(bucket=bucket, **kwargs)
        if not fsspec:
            raise ImportWarning(f"fsspec not installed, can't open filesystem: {uri}")
        fs = fsspec.filesystem(protocol, bucket=bucket, **kwargs)
    if not for_write:
        return FileSystemReadOnly(fs)
    return fs


def adapt_fsspec_storage_options(opts: dict) -> dict:
    """
    Adapt named arguments to work with fsspec.open().

    :param opts:  A 'kwargs' set of named parameters with either 'storage_options: dict', or parameters like
                    'access_key'.

    :returns:  A {} with options named as fsspec.open() expects, i.e. {"storage_options": {"key": "xyz"}} instead of
                access_key="xyz"
    """
    opts = dict(opts)
    storage_options = opts.pop("storage_options", None) or {}
    for k, k2 in KNOWN_FSSPEC_STORAGE_OPTIONS.items():
        if k in opts:
            storage_options[k2] = opts.pop(k)
        if k2 in opts:
            storage_options[k2] = opts.pop(k2)
    if storage_options:
        opts["storage_options"] = storage_options
    return opts


def is_breakout_path(path: str) -> bool:
    """
    Determine whether a path attempts to 'escape' to its parent or siblings.
    """
    level = 0
    for elem in path.split("/"):
        if elem in ("", "."):
            # empty
            continue
        if elem == "..":
            # up
            level -= 1
            if level < 0:
                return True
        else:
            # down
            level += 1
    return False


def join_uri_path(base_uri: str, *paths_to_add, no_breakout: bool=True) -> str:
    """
    Like os.path.join(), only with support for URIs/URLs.

    Unlike os.path.join(), paths starting with '/' will not discard all prior paths, the '/' will be ignored.

    :param base_uri:        The folder or URL to append to.
    :param paths_to_add:    Path elements to add.
    :return:        New path or URL.
    """
    if "?" in base_uri:
        out, after = base_uri.split("?", maxsplit=1)
        after = "?" + after
    elif "#" in base_uri:
        out, after = base_uri.split("#", maxsplit=1)
        after = "#" + after
    else:
        out, after = base_uri, ""
    for path in paths_to_add:
        if is_breakout_path(path) and no_breakout:
            raise ValueError(f"invalid path element: {path}")
        if not out.endswith("/"):
            out += "/"
        out += path.strip("/")
    return out + after


KNOWN_FSSPEC_STORAGE_OPTIONS = {
    "access_key": "key", "secret_key": "secret", "service_account": "service_account",
    "account_name": "account_name", "account_key": "account_key"
}