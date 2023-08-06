"""
Communication via shared volume.

In order to truly 'lock down' user-supplied code, and elimate the security risks associated with giving it access
to the network, or in providing it credentials for communicating with external REST services, all of mmlibrary's
communications can be sent to a folder shared with a sidecar (or another mounted volume).  The sidecar then transfers
the requests and responses to a REST API.
"""
import base64
import json
import os
import threading
import time

from ..exceptions import *
from .to_rest import DSLibraryViaREST


class DSLibraryViaVolume(DSLibraryViaREST):
    def __init__(self, volume: str, spec: dict=None, _env: dict=None, response_wait_interval=0.01):
        super(DSLibraryViaVolume, self).__init__(url="", spec=spec)
        self._volume = volume
        self._request_no = 0
        self._lock = threading.Lock()
        self._response_wait_interval = response_wait_interval

    class Response(object):
        def __init__(self, content: bytes):
            self.content = content

        @property
        def text(self):
            return self.content.decode("utf-8")

    def _do_comm(self, method: str, path: str, params: dict=None, data=None, as_json: bool=True):
        """
        Creation of a file in the folder is equivalent to making a REST call.  The response is returned in a file with
        a related filename.
        """
        t_timeout = time.time() + self._timeouts[1]
        with self._lock:
            self._request_no += 1
            fn_rqst = os.path.join(self._volume, f"rqst_{self._request_no}.json")
            fn_resp = fn_rqst + ".response"
            fn_resp_meta = fn_rqst + ".response-meta"
            rqst = {
                "method": method, "path": path, "params": params, "data": data, "timeout": t_timeout, "as_json": as_json
            }
            if isinstance(data, (bytes, bytearray)):
                rqst["data"] = base64.b64encode(data).decode("utf-8")
                rqst["data_format"] = "base64"
            rq_content = json.dumps(rqst)
            with open(fn_rqst, 'w') as f_w:
                f_w.write(rq_content)
            # now we wait for a response...
            try:
                while True:
                    time.sleep(self._response_wait_interval)
                    if time.time() > t_timeout:
                        raise DSLibraryCommunicationError(f"timeout waiting for {path} request")
                    if os.path.exists(fn_resp_meta):
                        try:
                            # read metadata, determine response type
                            with open(fn_resp_meta, 'rb') as f_r:
                                meta = json.load(f_r)
                            xfer = meta.get("xfer")
                            if as_json is None:
                                as_json = xfer == "json"
                            # detect error
                            if "error_class" in meta:
                                err_c = meta["error_class"]
                                err_a = meta["error_args"]
                                err_cls = None
                                if err_c in globals():
                                    err_cls = globals()[err_c]
                                elif hasattr(__builtins__, err_c):
                                    err_cls = getattr(__builtins__, err_c)
                                else:
                                    # FIXME weirdly, this works but the above does not
                                    try:
                                        err_cls = __builtins__[err_c]
                                    except:
                                        pass
                                if not issubclass(err_cls, Exception):
                                    err_cls = Exception.__class__
                                    err_a.append(err_c)
                                raise err_cls(*err_a)
                            # read response
                            with open(fn_resp, 'rb') as f_r:
                                if as_json:
                                    resp = json.load(f_r)
                                else:
                                    # NOTE: the burden is on the other side to deliver the entire response 'atomically'
                                    resp = DSLibraryViaVolume.Response(f_r.read())
                        except ValueError:
                            continue
                        return resp
            finally:
                os.remove(fn_rqst)
                if os.path.exists(fn_resp):
                    os.remove(fn_resp)
