from json import JSONEncoder

from poker.model.card import Card


class CardEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Card):
            return {"suit": str(object.suit), "value": str(object.value)}
        else:
            return JSONEncoder.default(self, object)