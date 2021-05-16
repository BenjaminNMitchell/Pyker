from json import JSONEncoder

from poker.encoders.json.card import CardEncoder
from poker.encoders.json.player import PlayerEncoder
from poker.model.actions import Action, ActionWithAmount, ActionWithCards


class ActionEncoder(JSONEncoder):
    """Serializer for action objects""" 


    def default(self, object):
        if isinstance(object, Action):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().default(object.player),
            }
        return JSONEncoder.default(self, object)


class ActionWithAmountEncoder(JSONEncoder):
    """Serializer for ActionWithAmount objects"""

    def default(self, object):
        if isinstance(object, ActionWithAmount):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().default(object.player),
                "amount": str(object.amount),
            }
        return JSONEncoder.default(self, object)


class ActionWithCardsEncoder(JSONEncoder):
    """Serializer for ActionWithCards objects"""
    def default(self, object):
        if isinstance(object, ActionWithCards):
            c_encoder = CardEncoder()
            p_encoder = PlayerEncoder()

            return {
                "type": object.__class__.__name__.lower(),
                "player": p_encoder.default(object.player),
                "cards": [c_encoder.default(x) for x in object.cards],
            }
        return JSONEncoder.default(self, object)
