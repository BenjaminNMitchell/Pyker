"""This module contains different player actions."""

from dataclasses import dataclass


@dataclass
class Action:
    player: str

    def __str__(self):
        return f"{self.player} {self.__class__.__name__.lower()}s"

    def __repr__(self):
        return f"{ self.__class__.__name__ }(player='{self.player}')"


class Check(Action):
    pass


class Fold(Action):
    pass


@dataclass
class ActionWithAmount:
    player: str
    amount: str

    def __str__(self):
        return f"{self.player} {self.__class__.__name__.lower()}s {self.amount}"

    def __repr__(self):
        return (
            f"{ self.__class__.__name__ }(player='{self.player}', amount={self.amount})"
        )


class Bet(ActionWithAmount):
    pass


class Raise(ActionWithAmount):
    pass


class Post(ActionWithAmount):
    pass


class Call(ActionWithAmount):
    pass
