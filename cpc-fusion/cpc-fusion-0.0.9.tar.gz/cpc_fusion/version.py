from cpc_fusion.module import (
    Module,
)


class Version(Module):
    @property
    def api(self):
        from cpc_fusion import __version__
        return __version__

    @property
    def node(self):
        return self.web3.manager.request_blocking("web3_clientVersion", [])

    @property
    def network(self):
        return self.web3.manager.request_blocking("net_version", [])

    @property
    def ethereum(self):
        return self.web3.manager.request_blocking("eth_protocolVersion", [])
