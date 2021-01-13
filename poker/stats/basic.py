from poker.model.actions import Bet, Raise, Call


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