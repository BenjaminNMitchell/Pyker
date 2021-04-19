"""This module defines a hand of texas holdem."""

from typing import List, Tuple, Set
from dataclasses import dataclass

from pandas.core.indexes.interval import interval_range

from poker.model import street
from poker.model import card
from poker.model import player


@dataclass
class Hand:
    """A hand of texas holdem."""

    id: int
    stacks: List[Tuple[player.Player, int]]
    players: Set[player.Player]
    our_cards: Tuple[card.Card]
    preflop: street.Street
    flop: Tuple[card.Card]
    first: street.Street
    turn: Tuple[card.Card]
    second: street.Street
    river: Tuple[card.Card]
    third: street.Street
    # TODO implement showdowns in the parser?
    # #showdown: Set[Tuple[card.Card]]

    def __str__(self):
        player_string = ", ".join([str(player) for player in self.players])
        return (
            "----Hand----\n"
            f"Players: {player_string}\n\n"
            f"Our Cards: {self.our_cards}\n"
            f"Pre Flop\n{self.preflop}\n\n"
            f"Flop: {str(self.flop)}\n"
            f"First Street\n{self.first}\n\n"
            f"Turn: {str(self.turn)}\n"
            f"Second Street\n{self.second}\n\n"
            f"River: {str(self.river)}\n"
            f"Third Street\n{self.third}\n"
        )
