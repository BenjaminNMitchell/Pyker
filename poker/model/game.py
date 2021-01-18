"""This module represents a game of texas holdem."""

from typing import Tuple
from typing import Set

from dataclasses import dataclass

from poker.model import hand
from poker.model import player


class Game:
    def __init__(self, hands: Tuple[hand.Hand]):
        self.hands = hands
        self.players = set().union(*[hand.players for hand in hands])