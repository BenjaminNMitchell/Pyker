""" This Module contains different admin actions. """

from dataclasses import dataclass
from typing import Tuple

from poker.model.card import Card
from poker.model.player import Player


@dataclass
class AdminAction:
    """A generic object representing admin actions """

    player: Player


class BuyIn(AdminAction):
    """An Object indicating that the admin added chips to a player's stack"""

    amount: int
    hand: int

    def __str__(self):
        return f"{self.player} buys in for {self.amount}"
