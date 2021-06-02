"""JSON encoder for Player object"""
from json import JSONEncoder

from poker.model.player import Player


class PlayerEncoder(JSONEncoder):
    """Encoder class for Player object"""

    def encode(self, object):
        """Player to JSON"""
        if isinstance(object, Player):
            return {"name": object.name, "id_": str(object.id_)}
        return JSONEncoder.default(self, object)
