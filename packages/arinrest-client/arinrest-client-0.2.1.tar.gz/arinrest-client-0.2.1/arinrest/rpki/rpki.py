from arinrest.common.connection import ArinRestConnection
from arinrest.common.rsa import RSASigner
from arinrest.rpki.roa import ROA


class Rpki(object):
    def init(self, connection: ArinRestConnection, private_key: str):

        self.connection = connection
        self.roas = []
        self.signer = RSASigner(private_key)

    def add_roa(self, roa: ROA) -> None:
        """sign and add ROA to RPKI session"""

        # sign the object and b64encode it on
        # string creation of the roa
        roa.signature = self.signer.sign(str(roa))
        self.roas.append(roa)

        return

    def submit_roas(self):
        """send roa creation request to ARIN"""
        for roa in self.roas:
            self.connection.post(url, roa.to_xml())
