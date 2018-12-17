"""
@file
@brief Server with :epkg:`hypercorn`.
"""
from hypercorn.config import Config
from hypercorn.run import run
from hypercorn.utils import load_application


class ServerHypercorn:
    """
    Implements a server based on :epkg:`hypercorn`.
    """

    def __init__(self, **kwargs):
        """
        @param      kwargs      parameters
        """
        self._run = run
        config = Config()
        app = load_application(kwargs['application_path'])
        if app is None:
            raise RuntimeError("Unable to load application '{0}'".format(
                kwargs["application_path"]))

        for k, v in kwargs.items():
            if k in ('binds',):
                continue
            setattr(config, k, v)

        if len(kwargs['binds']) > 0:
            config.update_bind(kwargs['binds'])
        self.config = config

    def run(self, verbose=True):
        """
        Starts the server.

        @param      verbose     display the host
        """
        if verbose:
            scheme = "https" if self.config.ssl_enabled else "http"
            print("[mathenjeu] running on {}://{}:{}".format(scheme, self.config.host,
                                                             self.config.port))
        self._run(self.config)
