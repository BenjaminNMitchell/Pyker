from json import JSONEncoder

from poker.encoders.json.card import CardEncoder
from poker.encoders.json.player import PlayerEncoder
from poker.model.actions import Action, ActionWithAmount, ActionWithCards


class ActionEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Action):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().default(object.player),
            }
        return JSONEncoder.default(self, object)


class ActionWithAmountEncoder:
    def default(self, object):
        if isinstance(object, ActionWithAmount):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().default(object.player),
                "amount": str(object.amount),
            }
        return JSONEncoder.default(self, object)


class ActionWithCardsEncoder:
    def default(self, object):
        if isinstance(object, ActionWithCards):
            c_encoder = CardEncoder()

            return {
                "type": object.__class__.__name__.lower(),
                "cards": [c_encoder.default(x) for x in object.cards],
            }
        return JSONEncoder.default(self, object)
