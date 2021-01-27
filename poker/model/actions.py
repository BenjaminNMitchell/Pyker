"""This module contains different player actions."""

from dataclasses import dataclass

from poker.model.player import Player


@dataclass
class Action:
    player: Player

    def __str__(self):
        return f"{self.player.name} {self.__class__.__name__.lower()}s"

    def __repr__(self):
        return f"{ self.__class__.__name__ }(player={repr(self.player)})"


class Check(Action):
    pass


class Fold(Action):
    pass


@dataclass
class ActionWithAmount:
    player: Player
    amount: int

    def __str__(self):
        return f"{self.player.name} {self.__class__.__name__.lower()}s {self.amount}"

    def __repr__(self):
        return f"{ self.__class__.__name__ }(player={repr(self.player)}, amount={self.amount})"


class Bet(ActionWithAmount):
    pass


class Raise(ActionWithAmount):
    pass


class Post(ActionWithAmount):
    pass


class Call(ActionWithAmount):
    pass
