"""JSON encoder for street object"""
from json import JSONEncoder

from poker.model.street import Street
from poker.model.actions import Action, ActionWithAmount, ActionWithCards
from poker.encoders.json.actions import (
    ActionEncoder,
    ActionWithAmountEncoder,
    ActionWithCardsEncoder,
)


class StreetEncoder(JSONEncoder):
    """Extends JSONEncoder for Street object"""

    def default(self, object):
        """Street -> JSON"""
        if isinstance(object, Street):

            a_encoder = ActionEncoder()
            awa_encoder = ActionWithAmountEncoder()
            awc_encoder = ActionWithCardsEncoder()

            serialized = []

            for action in object.actions:

                if isinstance(action, Action):
                    json_repr = a_encoder.default(action)

                if isinstance(action, ActionWithAmount):
                    json_repr = awa_encoder.default(action)

                if isinstance(action, ActionWithCards):
                    json_repr = awc_encoder.default(action)

                serialized.append(json_repr)

        return {"actions": serialized}
