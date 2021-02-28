"""This module defines a hand of texas holdem."""

from typing import Tuple, Set
from dataclasses import dataclass

from poker.model import street
from poker.model import card
from poker.model import player

@dataclass
class Hand:
    """A hand of texas holdem."""

    stacks: Set[(player.Player, int)]
    players: Set[player.Player]
    our_cards: Tuple[card.Card]
    preflop: street.Street
    flop: Tuple[card.Card]
    first: street.Street
    turn: Tuple[card.Card]
    second: street.Street
    river: Tuple[card.Card]
    third: street.Street

    def __str__(self):
        player_string = ", ".join([str(player) for player in self.players])
        return (
            "----Hand----\n"
            f"Players: {player_string}\n\n"
            f"Our Cards: {self.our_cards}\n"
            f"Pre Flop\n{self.preflop}\n\n"
            f"Flop: {self.flop}\n"
            f"First Street\n{self.first}\n\n"
            f"Turn: {self.turn}\n"
            f"Second Street\n{self.second}\n\n"
            f"River: {self.river}\n"
            f"Third Street\n{self.third}\n"
        )
