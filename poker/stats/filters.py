"""This module defines a set of filters to catagorize hands."""


from poker.model.actions import Raise
from poker.model.hand import Hand
from poker.model.player import Player


def player_open_raised(hand: Hand, player: Player):
    """Return true if the player open raise during the hand."""
    for action in hand.preflop:
        if isinstance(action, Raise) and action.player == player:
            return True

    return False
