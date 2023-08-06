"""
The 'other side' of communications for MMLibraryViaVolume.  Watches for requests appearing in a folder as JSON
files, and transmits them to a remote REST API.
"""
import base64
import os
import json
import time

from ..front import DSLibrary
from .. import _DEFAULT as DEFAULT_DSLIBRARY


class VolumeWatcher(object):
    def __init__(self, volume: str, target_dslibrary: DSLibrary):
        self._volume = volume
        self._target = target_dslibrary or DEFAULT_DSLIBRARY

    def scan_forever(self, callback=None, interval: float=0.05, check_signals: bool=False):
        """
        Scan repeatedly.  The supplied callback can raise an exception to stop the process.

        :param callback:        This method will be called before every scan of the volume.  You can use it to exit,
                                check for special messages, etc..
        :param interval:        How often to scan.
        :param check_signals:   Whether to exit on SIGINT or SIGTERM.
        """
        running = [True]
        if check_signals:
            # stop on SIGINT
            import signal
            def signal_handler(sig, frame):
                running[0] = False
            signal.signal(signal.SIGTERM, signal_handler)
            signal.signal(signal.SIGINT, signal_handler)
        try:
            while running[0]:
                time.sleep(interval)
                if callback:
                    callback()
                self.scan_once()
        except StopIteration:
            pass

    def scan_once(self):
        """
        Scan for new requests.
        """
        for f in os.listdir(self._volume):
            if not f.endswith(".json"):
                continue
            try:
                fn = os.path.join(self._volume, f)
                with open(fn) as f_r:
                    request = json.load(f_r)
            except ValueError:
                continue
            try:
                had_error = False
                response = self.process(request)
            except Exception as err:
                had_error = True
                response = {
                    "error_class": err.__class__.__name__,
                    "error_args": err.args
                }
            # send response (if request file still exists)
            if os.path.exists(fn):
                response_fn = fn + ".response"
                response_meta_fn = fn + ".response-meta"
                response_tmp = fn + ".tmp"
                # write to temporary file
                with open(response_tmp, 'wb') as f_w:
                    if isinstance(response, (bytes, bytearray)):
                        response_xfer = "binary"
                        f_w.write(response)
                    elif isinstance(response, str):
                        response_xfer = "text"
                        f_w.write(response.encode("utf-8"))
                    else:
                        response_xfer = "json"
                        resp_s = json.dumps(response)
                        f_w.write(resp_s.encode("utf-8"))
                # rename to expected location
                os.rename(response_tmp, response_fn)
                # metadata
                meta = response if had_error else {"xfer": response_xfer, "type": response.__class__.__name__}
                with open(response_meta_fn, 'wb') as f_w:
                    f_w.write(json.dumps(meta).encode("utf-8"))

    def process(self, request: dict):
        """
        Process a single request.
        """
        data = request.get("data")
        data_format = request.get("data_format")
        if data_format == "base64":
            data = base64.b64decode(data)
        # if the target has a communication method we can just forward everything directly
        if hasattr(self._target, "_do_comm"):
            return self._target._do_comm(
                method=request["method"], path=request["path"], params=request["params"],
                data=data, as_json=request["as_json"]
            )
        # otherwise we have to actually interpret the request
        path_parts = request["path"].split("/")
        method_path0 = f"{request['method']}:{path_parts[0]}"
        params = request.get("params", {})
        path = "/".join(path_parts[1:])
        resource_name = params.pop("resource_name", '')
        if resource_name:
            if resource_name.startswith("../") or "/../" in resource_name or resource_name.endswith("/..") or resource_name == "..":
                raise ValueError("break-out path blocked")
            path = os.path.join(path, resource_name)
        # read file content
        if method_path0 in ("get:resources", "get:run_data"):
            if method_path0 == "get:run_data":
                opener = self._target.open_run_data
            else:
                opener = self._target.open_resource
            with opener(path, mode='rb', **params) as f_r:
                if "byte_range" in params:
                    byte_range = json.loads(params["byte_range"])
                    f_r.seek(byte_range[0])
                    return f_r.read(byte_range[1] - byte_range[0])
                else:
                    return f_r.read()
        # write file content
        if method_path0 in ("put:resources", "put:run_data"):
            if method_path0 == "put:run_data":
                writer = self._target.write_run_data
            else:
                writer = self._target.write_resource
            writer(path, content=data, **params)
            return {}
        # get metadata and parameters
        if method_path0 == "get:context":
            return {
                "metadata": self._target.get_metadata().to_json(),
                "parameters": self._target.get_parameters()
            }
        # scoring requests
        if method_path0 == "get:scoring-requests":
            request = self._target.next_scoring_request(timeout=params.get("timeout"))
            if request:
                return {"request": request}
            return {}
        if method_path0 == "post:score":
            self._target.scoring_response(params.get("score"))
            return {}
        # database r/w
        if method_path0 == "get:db":
            sql = params.get("sql")
            parameters = params.get("parameters")
            with self._target.get_sql_connection(path) as conn:
                c = conn.cursor()
                c.execute(sql, parameters)
                descr = c.description
                rows = list(c)
                more = False
            return [descr, rows, more]
        if method_path0 == "get:db_more":
            pass
        if method_path0 == "post:db":
            sql = params.get("sql")
            parameters = params.get("parameters")
            with self._target.get_sql_connection(path, for_write=True) as conn:
                c = conn.cursor()
                c.execute(sql, parameters)
            return {}
        # unrecognized
        raise Exception(f"not implemented yet: {method_path0}")
