"""Json Encoder for card Object"""

from poker.model.card import Card
from poker.encoders.json.exceptions import UnsupportedObjectToJSON


class CardEncoder:
    """Card object to JSON"""

    def encode(self, obj):
        """Card -> JSON"""
        if isinstance(obj, Card):
            return {"suit": str(obj.suit), "value": str(obj.value)}

        raise UnsupportedObjectToJSON(f"CardEncoder called on {type(obj)}")
