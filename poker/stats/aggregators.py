"""This module contains logic to calculate some common statisic for games."""

from typing import Dict, Callable

import pandas as pd

from poker.model.game import Game
from poker.model.player import Player
from poker.model.hand import Hand
from poker.stats import indicators
from poker.stats import metrics


def get_game_stats(game: Game) -> pd.DataFrame:
    """Return the statistics from a Game of texas holdem"""

    vpip = average_over_game(game, indicators.get_vpip_players)
    pre_flop_raise = average_over_game(game, indicators.get_pfr_players)
    hands_dealt = count_over_game(game, indicators.get_dealt_players)
    aggression_factor = get_game_metric(game, metrics.get_aggression_factor)

    stats = {
        "Hands": hands_dealt,
        "VPIP": vpip,
        "PFR": pre_flop_raise,
        "AF": aggression_factor,
    }
    df_stats = pd.DataFrame(stats)
    return df_stats


def count_over_game(
    game: Game, indicator: Callable[[Hand], indicators.Indications]
) -> Dict[Player, int]:
    """
    Return counts per player for occurences of an event defined buy
    the supplied indicator function.
    """

    counts = {player: 0 for player in game.players}

    for hand in game.hands:
        for player, _ in indicator(hand).items():
            counts[player] += 1

    return counts


def average_over_game(
    game: Game, indicator: Callable[[Hand], indicators.Indications]
) -> Dict[Player, float]:
    """Average an indication over a game."""

    game_metrics = {
        player: metrics.Metric(numerator=0, denominator=0) for player in game.players
    }

    for hand in game.hands:
        for player, is_stat in indicator(hand).items():
            game_metrics[player].denominator += 1

            if is_stat:
                game_metrics[player].numerator += 1

    return {player: metric.to_fraction() for player, metric in game_metrics.items()}


def get_game_metric(game: Game, metricator: Callable[[Hand], metrics.Metrics]):
    """Return a metric calculated over a game."""

    game_metrics = {
        player: metrics.Metric(numerator=0, denominator=0) for player in game.players
    }

    for hand in game.hands:
        hand_metrics = metricator(hand)
        for player, metric in hand_metrics.items():
            game_metrics[player] += metric

    return {player: metric.to_fraction() for player, metric in game_metrics.items()}
