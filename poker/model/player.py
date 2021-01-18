"""The module contains information on players."""

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    id_: str

    def __hash__(self):
        return hash(self.id_)

    def __eq__(self, other):
        return isinstance(other, Player) and self.id_ == other.id_
