"""JSON encoder for Hand object"""
from json import JSONEncoder

from poker.model.hand import Hand

from poker.encoders.json.player import PlayerEncoder
from poker.encoders.json.street import StreetEncoder
from poker.encoders.json.card import CardEncoder


class HandEncoder(JSONEncoder):
    """Encoder for Hand Object"""

    def encode(self, object):
        """Hand to JSON"""
        if isinstance(object, Hand):
            json_repr = {}

            p_encoder = PlayerEncoder()
            c_encoder = CardEncoder()
            s_encoder = StreetEncoder()

            json_repr["id_"] = str(object.id_)
            json_repr["players"] = [p_encoder.encode(x) for x in object.players]

            json_repr["stacks"] = {}

            for p in object.stacks.keys():
                json_repr["stacks"][p.name.lower()] = str(object.stacks[p])

            json_repr["our_cards"] = [c_encoder.encode(x) for x in object.our_cards]
            json_repr["preflop"] = s_encoder.encode(object.preflop)

            if object.first:
                json_repr["first"] = s_encoder.encode(object.first)
            if object.second:
                json_repr["second"] = s_encoder.encode(object.second)
            if object.third:
                json_repr["third"] = s_encoder.encode(object.third)

            if object.flop:
                json_repr["flop"] = [c_encoder.encode(x) for x in object.flop]
            if object.turn:
                json_repr["turn"] = [c_encoder.encode(x) for x in object.turn]
            if object.river:
                json_repr["river"] = [c_encoder.encode(x) for x in object.river]

            return json_repr

        return JSONEncoder.encode(object)
