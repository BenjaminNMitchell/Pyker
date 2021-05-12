from json import JSONEncoder

from poker.model.street import Street
from poker.model.actions import Action, ActionWithAmount, ActionWithCards
from poker.encoders.json.actions import (
    ActionEncoder,
    ActionWithAmountEncoder,
    ActionWithCardsEncoder,
)


class StreetEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Street):

            a_encoder = ActionEncoder()
            awa_encoder = ActionWithAmountEncoder()
            awc_encoder = ActionWithCardsEncoder()

            serialized = []

            for action in object.actions:

                if object.__class__ == Action:
                    json_repr = a_encoder.default(object)

                if object.__class__ == ActionWithAmount:
                    json_repr = awa_encoder.default(object)

                if object.__class__ == ActionWithCards:
                    json_repr = awa_encoder.default(object)

                serialized.append(json_repr)
        return {"actions": serialized}
