"""Json Encoders for Action, ActionWithAmount, ActionWithCards objs"""

from poker.encoders.json.exceptions import UnsupportedObjectToJSON
from poker.encoders.json.card import CardEncoder
from poker.encoders.json.player import PlayerEncoder
from poker.model.actions import Action, ActionWithAmount, ActionWithCards


class ActionEncoder:
    """Serializer for action objects"""

    def encode(self, obj):
        """Action -> JSON"""
        if isinstance(obj, Action):
            return {
                "type": obj.__class__.__name__.lower(),
                "player": PlayerEncoder().encode(obj.player),
            }
        raise UnsupportedObjectToJSON(f"ActionEncoder called on {type(obj)}")


class ActionWithAmountEncoder:
    """Serializer for ActionWithAmount objects"""

    def encode(self, obj):
        """ActionWithAmount -> JSON"""
        if isinstance(obj, ActionWithAmount):
            return {
                "type": obj.__class__.__name__.lower(),
                "player": PlayerEncoder().encode(obj.player),
                "amount": str(obj.amount),
            }

        raise UnsupportedObjectToJSON(f"ActionWithAmountEncoder called on {type(obj)}")


class ActionWithCardsEncoder:
    """Serializer for ActionWithCards objects"""

    def encode(self, obj):
        """ActionWithCards -> JSON"""
        if isinstance(obj, ActionWithCards):
            c_encoder = CardEncoder()
            p_encoder = PlayerEncoder()

            return {
                "type": obj.__class__.__name__.lower(),
                "player": p_encoder.encode(obj.player),
                "cards": [c_encoder.encode(x) for x in obj.cards],
            }
        raise UnsupportedObjectToJSON(f"ActionWithCardEncoder called on {type(obj)}")
