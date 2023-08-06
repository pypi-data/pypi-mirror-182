from arinrest.common.connection import ArinRestConnection


class Route(object):
    def __init__(self, connection: ArinRestConnection):
        self.connection = connection
