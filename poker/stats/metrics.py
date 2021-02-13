"""This module defines various metrics about poker hands."""

from dataclasses import dataclass
import typing

import numpy as np

from poker.model.actions import Bet, Raise, Call
from poker.model.hand import Hand
from poker.model.player import Player


@dataclass
class Metric:
    """A metric is defined by some kind of statistic with a numerator and denominator."""

    numerator: float
    denominator: float

    def __add__(self, other):
        if not isinstance(other, Metric):
            raise ValueError(
                f"addition is not defined between Metric and {type(other)}"
            )

        return Metric(
            numerator=self.numerator + other.numerator,
            denominator=self.denominator + other.denominator,
        )

    def to_fraction(self):
        """Return the metric as a fraction."""

        if self.denominator == 0:
            return np.Inf

        return self.numerator / self.denominator


Metrics = typing.NewType("Metrics", typing.Dict[Player, Metric])


def get_aggression_factor(hand: Hand) -> Metrics:
    """Return a metric representation of each players Agression Factor."""

    aggressive_counts = _count_actions_post_flop(hand, (Bet, Raise))
    passive_counts = _count_actions_post_flop(hand, (Call,))

    metrics = {}
    for player in hand.players:
        metrics[player] = Metric(
            numerator=aggressive_counts[player], denominator=passive_counts[player]
        )

    return Metrics(metrics)


def _count_actions_post_flop(hand: Hand, valid_types: typing.Tuple) -> typing.Dict:

    counts = {player: 0 for player in hand.players}

    streets = filter(
        lambda street: street is not None, [hand.first, hand.second, hand.third]
    )

    for street in streets:
        for action in street:
            if isinstance(action, valid_types):
                counts[action.player] += 1

    return counts
