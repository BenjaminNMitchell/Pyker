"""
This module defines various indication functions for poker hands.

An indication function is a function which that indicates which players have a given property.
"""

import typing

from poker.model.actions import Bet, Raise, Call
from poker.model.hand import Hand
from poker.model.player import Player


Indications = typing.Dict[Player, bool]


def get_vpip_players(hand: Hand) -> Indications:
    """
    Return an indication of the players that were VPIP for the hand.
    Voluntary Put In Pot (VPIP) means the player volunteered to put money into the pot pre-flop.
    """

    return _get_players_making_actions(hand.preflop, (Bet, Raise, Call))


def get_pfr_players(hand: Hand) -> Indications:
    """
    Return an indication of the players that were PFR for the hand.

    Pre Flop Raise (PFR) Means that the player raised the stakes preflop.
    """

    return _get_players_making_actions(hand.preflop, (Bet, Raise))


def get_dealt_players(hand: Hand) -> Indications:
    """
    Return an indication of the players that were dealt into the hand.
    """

    return {player: True for player in hand.players}


def _get_players_making_actions(street, valid_types):
    info = {}
    for action in street:
        is_volentary = isinstance(action, valid_types)
        if is_volentary or action.player not in info:
            info[action.player] = is_volentary
    return info
