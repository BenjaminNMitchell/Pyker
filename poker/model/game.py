"""This module represents a game of texas holdem."""


from typing import Set, Tuple

from poker.model import hand
from poker.model.player import Player
from poker.model.admin import BuyIn

class Game:
    """A game of no limit texas holdem."""

    def __init__(self, hands: Tuple[hand.Hand]):
        self.hands = hands
        self.players: Set[Player] = set()
        self.buyins: Set[BuyIn]
        self.cashouts: Set[CashOut]
        for hand in hands:
            self.players.union(hand.players)
