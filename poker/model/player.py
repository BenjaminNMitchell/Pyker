"""The module contains information on players."""

from dataclasses import dataclass


@dataclass
class Player:
    """A player in a game of poker."""

    name: str
    id_: str

    def __hash__(self):
        return hash(self.id_)

    def __eq__(self, other):
        return isinstance(other, Player) and self.id_ == other.id_

    def __str__(self):
        return self.name
