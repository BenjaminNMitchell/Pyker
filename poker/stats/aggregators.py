"""This module contains logic to calculate some common statisic for games."""

import logging

import pandas as pd
import numpy as np

from poker.model.game import Game
from poker.stats import indicators


def get_game_stats(game: Game):

    vpip = average_over_game(game.hands, indicators.get_vpip_players)
    pre_flop_raise = average_over_game(game.hands, indicators.get_pfr_players)
    aggression_factor = get_aggression_factor(game)

    stats = {"VPIP": vpip, "PFR": pre_flop_raise, "AF": aggression_factor}
    df = pd.DataFrame(stats)
    return df


def average_over_game(hands, func):

    hands_in = {}
    hands_with_stat = {}

    for hand in hands:
        info = func(hand)

        for player, is_stat in info.items():
            if player not in hands_in:
                hands_in[player] = 0

            hands_in[player] += 1

            if player not in hands_with_stat:
                hands_with_stat[player] = 0

            if is_stat:
                hands_with_stat[player] += 1

    percentage_vpip = {}
    for player in hands_in:
        percentage_vpip[player] = hands_with_stat[player] / hands_in[player]

    return percentage_vpip


def get_aggression_factor(game: Game):
    game_aggressive_actions_counts = {player: 0 for player in game.players}

    for hand in game.hands:
        for player, count in indicators.count_agressive_actions(hand).items():
            game_aggressive_actions_counts[player] += count

    logging.debug("Game Aggressive Counts: %s", game_aggressive_actions_counts)
    game_call_counts = {player: 0 for player in game.players}
    for hand in game.hands:
        for player, count in indicators.count_calls(hand).items():
            game_call_counts[player] += count

    logging.debug("Game Calls Counts: %s", game_call_counts)
    aggression_factors = {player: None for player in game.players}
    for player in game.players:
        num_calls = game_call_counts[player]
        num_aggresive = game_aggressive_actions_counts[player]

        if num_calls == 0:
            if num_aggresive > 0:
                aggression_factors[player] = np.Inf
        else:
            aggression_factors[player] = num_aggresive / num_calls
    return aggression_factors