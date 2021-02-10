"""This module contains different player actions."""

from dataclasses import dataclass

from poker.model.player import Player


@dataclass
class Action:
    """A generic player Action."""

    player: Player

    def __str__(self):
        return f"{self.player.name} {self.__class__.__name__.lower()}s"

    def __repr__(self):
        return f"{ self.__class__.__name__ }(player={repr(self.player)})"


class Check(Action):  # pylint: disable=too-few-public-methods
    """A check action which signifies the player does nothing."""


class Fold(Action):  # pylint: disable=too-few-public-methods
    """A fold action which signifies the player abandoned the hand."""


@dataclass
class ActionWithAmount:
    """A generic action that has an associated player and amount."""

    player: Player
    amount: int

    def __str__(self):
        return f"{self.player.name} {self.__class__.__name__.lower()}s {self.amount}"

    def __repr__(self):
        return f"{ self.__class__.__name__ }(player={repr(self.player)}, amount={self.amount})"


class Bet(ActionWithAmount):  # pylint: disable=too-few-public-methods
    """
    A bet action which signifies the player added chips to the pot and
    was the first player to do so in the street.
    """


class Raise(ActionWithAmount):  # pylint: disable=too-few-public-methods
    """
    A raise action which signifies the player added chips to the pot and
    was not the first player to do so in the street.
    """


class Post(ActionWithAmount):  # pylint: disable=too-few-public-methods
    """
    A post action which signifies the player was forced to add chips to
    the pot to cover blinds.
    """


class Call(ActionWithAmount):  # pylint: disable=too-few-public-methods
    """
    A call action which signifies the player added chips to the pot to match
    a bet or raise.
    """

class Collect(ActionWithAmount): # pylint: disable=too-few-public-methods
    """
    A call action which signifies the player added chips to the pot to match
    a bet or raise.
    """
