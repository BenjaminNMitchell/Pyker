"""This module represents a game of texas holdem."""


from typing import Set, Tuple

from poker.model import hand
from poker.model.player import Player


class Game:
    """A game of no limit texas holdem."""

    def __init__(self, hands: Tuple[hand.Hand]):
        """Construct a game from a collection of hands"""
        self.hands = hands
        self.players: Set[Player] = set()
        for hand_ in hands:
            self.players = self.players.union(hand_.players)
