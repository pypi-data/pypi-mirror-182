from arinrest.common.connection import ArinRestConnection
from arinrest.rpki.rpki import Rpki
from arinrest.irr.route import Route
from arinrest.rdap import RdapClient
from typing import Union


class ArinRest(object):
    def __init__(
        self,
        api_key: Union[str, None],
    ) -> None:
        self.api_key = api_key

    def rpki(self, **kwargs):
        connection = ArinRestConnection("rpki", self.api_key, **kwargs)
        return Rpki(connection)

    def irr(self, **kwargs):
        self.connection = ArinRestConnection("irr", self.api_key, **kwargs)
        self.route = Route(self.connection)
        return self

    def rdap(self, **kwargs):
        connection = ArinRestConnection("rdap", None)
        return RdapClient(connection)
