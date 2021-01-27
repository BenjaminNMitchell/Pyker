"""This module defines common queries of hands."""

from poker.model.actions import Bet, Raise, Call, Check


def get_vpip_players(hand):
    return _get_players_making_actions(hand.preflop, (Bet, Raise, Call))


def get_pfr_players(hand):
    return _get_players_making_actions(hand.preflop, (Bet, Raise))


def _get_players_making_actions(actions, valid_types):
    info = {}
    for action in actions:
        is_volentary = isinstance(action, valid_types)
        if is_volentary or action.player not in info:
            info[action.player] = is_volentary
    return info


def count_agressive_actions(hand):

    return _count_actions_post_flop(hand, (Bet, Raise))

def count_calls(hand):

    return _count_actions_post_flop(hand, (Call))
    


def _count_actions_post_flop(hand, valid_types):

    counts = {}

    for street in [hand.first, hand.second, hand.third]:
        if street is None:
            break

        for action in street:
            if isinstance(action, valid_types):

                if action.player not in counts:
                    counts[action.player] = 1
                else:
                    counts[action.player] += 1

    return counts