from json import JSONEncoder

from poker.model.player import Player


class PlayerEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Player):
            return {"name": object.name, "id_": str(object.id_)}
        else:
            return JSONEncoder.default(self, object)
