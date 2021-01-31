"""This module represents a game of texas holdem."""

from typing import Tuple

from poker.model import hand


class Game:
    """A game of no limit texas holdem."""

    def __init__(self, hands: Tuple[hand.Hand]):
        self.hands = hands
        self.players = set().union(*[hand.players for hand in hands])
