"""This module defines a street or round of betting."""

from dataclasses import dataclass
from typing import List, Union

from poker.model import actions


@dataclass
class Street:
    """A Street is defined as a round of betting which consists of a list of player actions."""

    actions: List[Union[actions.ActionWithAmount, actions.Action]]

    def __iter__(self):
        return iter(self.actions)

    def __repr__(self):
        return f"Street(actions={repr(self.actions)})"

    def __str__(self):
        return "\n".join([str(action) for action in self.actions])
