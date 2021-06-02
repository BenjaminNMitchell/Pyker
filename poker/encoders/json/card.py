"""Json Encoder for card Object"""

from json import JSONEncoder

from poker.model.card import Card
from poker.encoders.json.exceptions import UnsupportedObjectToJSON


class CardEncoder:
    """Card object to JSON"""

    def encode(self, object):
        if isinstance(object, Card):
            return {"suit": str(object.suit), "value": str(object.value)}

        raise UnsupportedObjectToJSON(f"CardEncoder called on {type(object)}")
