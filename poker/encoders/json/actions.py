"""Json Encoders for Action, ActionWithAmount, ActionWithCards objects"""
from json import JSONEncoder

from poker.encoders.json.exceptions import UnsupportedObjectToJSON
from poker.encoders.json.card import CardEncoder
from poker.encoders.json.player import PlayerEncoder
from poker.model.actions import Action, ActionWithAmount, ActionWithCards


class ActionEncoder:
    """Serializer for action objects"""

    def encode(self, object):
        if isinstance(object, Action):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().encode(object.player),
            }
        raise UnsupportedObjectToJSON(f"ActionEncoder called on {type(object)}")


class ActionWithAmountEncoder:
    """Serializer for ActionWithAmount objects"""

    def encode(self, object):
        if isinstance(object, ActionWithAmount):
            return {
                "type": object.__class__.__name__.lower(),
                "player": PlayerEncoder().encode(object.player),
                "amount": str(object.amount),
            }

        raise UnsupportedObjectToJSON(
            f"ActionWithAmountEncoder called on {type(object)}"
        )


class ActionWithCardsEncoder:
    """Serializer for ActionWithCards objects"""

    def encode(self, object):
        if isinstance(object, ActionWithCards):
            c_encoder = CardEncoder()
            p_encoder = PlayerEncoder()

            return {
                "type": object.__class__.__name__.lower(),
                "player": p_encoder.encode(object.player),
                "cards": [c_encoder.encode(x) for x in object.cards],
            }
        raise UnsupportedObjectToJSON(f"ActionWithCardEncoder called on {type(object)}")
