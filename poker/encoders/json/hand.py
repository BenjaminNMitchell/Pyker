
from json import JSONEncoder

from poker.model.player import Player
from poker.model.street import Street
from poker.model.hand import Hand

from poker.encoders.json.player import PlayerEncoder
from poker.encoders.json.street import StreetEncoder
from poker.encoders.json.card import CardEncoder

class HandEncoder(JSONEncoder):
    def default(self, object):
        
        if isinstance(object, Hand):
            json_repr = {}

            p_encoder = PlayerEncoder()
            c_encoder = CardEncoder()
            s_encoder = StreetEncoder()
            
            json_repr['id'] = str(object.id)
            json_repr['players'] = [p_encoder(x) for x in object.players]

            #TODO impliment encoder support for player starting stacks
            #consider refactoring starting stacks to a dict: player -> int

            json_repr['our_cards'] = [c_encoder(x) for x in object.our_cards]
            json_repr['preflop'] = s_encoder(object.preflop)
            json_repr['first'] = s_encoder(object.first)
            json_repr['second'] = s_encoder(object.second)
            json_repr['third'] = s_encoder(object.third)
            
            json_repr['flop'] = [c_encoder(x) for x in object.flop]
            json_repr['turn'] = [c_encoder(x) for x in object.turn]
            json_repr['river'] = [c_encoder(x) for x in object.river]

            return json_repr

        return JSONEncoder.default(object)


