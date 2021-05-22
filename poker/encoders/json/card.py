"""Json Encoder for card Object"""

from json import JSONEncoder

from poker.model.card import Card


class CardEncoder(JSONEncoder):
    """Card object to JSON"""

    def default(self, object):
        if isinstance(object, Card):
            return {"suit": str(object.suit), "value": str(object.value)}

        return JSONEncoder.default(self, object)
