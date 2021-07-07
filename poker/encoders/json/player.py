"""JSON encoder for Player object"""

from poker.encoders.json.exceptions import UnsupportedObjectToJSON
from poker.model.player import Player


class PlayerEncoder:
    """Encoder class for Player object"""

    def encode(self, obj):
        """Player to JSON"""
        if isinstance(obj, Player):
            return {"name": obj.name, "id_": str(obj.id_)}

        raise UnsupportedObjectToJSON(f"Player encoder called on {type(obj)}")
