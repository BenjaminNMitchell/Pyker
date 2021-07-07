"""JSON encoder for Hand object"""

from poker.encoders.json.exceptions import UnsupportedObjectToJSON
from poker.model.hand import Hand

from poker.encoders.json.player import PlayerEncoder
from poker.encoders.json.street import StreetEncoder
from poker.encoders.json.card import CardEncoder


class HandEncoder:
    """Encoder for Hand Object"""

    def encode(self, obj):
        """Hand to JSON"""
        if isinstance(obj, Hand):
            json_repr = {}

            p_encoder = PlayerEncoder()
            c_encoder = CardEncoder()
            s_encoder = StreetEncoder()

            json_repr["id_"] = str(obj.id_)
            json_repr["players"] = [p_encoder.encode(x) for x in obj.players]

            json_repr["stacks"] = {}

            for p in obj.stacks.keys():
                json_repr["stacks"][p.name.lower()] = str(obj.stacks[p])

            json_repr["our_cards"] = [c_encoder.encode(x) for x in obj.our_cards]
            json_repr["preflop"] = s_encoder.encode(obj.preflop)

            if obj.first:
                json_repr["first"] = s_encoder.encode(obj.first)
            if obj.second:
                json_repr["second"] = s_encoder.encode(obj.second)
            if obj.third:
                json_repr["third"] = s_encoder.encode(obj.third)

            if obj.flop:
                json_repr["flop"] = [c_encoder.encode(x) for x in obj.flop]
            if obj.turn:
                json_repr["turn"] = [c_encoder.encode(x) for x in obj.turn]
            if obj.river:
                json_repr["river"] = [c_encoder.encode(x) for x in obj.river]

            return json_repr

        raise UnsupportedObjectToJSON(f"HandEncoder called on {type(obj)}")
