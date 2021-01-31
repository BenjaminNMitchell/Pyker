"""This module contains a card object."""

from dataclasses import dataclass

import enum


class Suits(enum.Enum):
    """A suit from a typical western deck of cards."""

    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


STRING_TO_SUIT_MAPPING = {
    "♠": Suits.SPADES,
    "S": Suits.SPADES,
    "♣": Suits.CLUBS,
    "C": Suits.CLUBS,
    "♥": Suits.HEARTS,
    "H": Suits.HEARTS,
    "♦": Suits.DIAMONDS,
    "D": Suits.DIAMONDS,
}
SUIT_TO_STRING_MAPPING = {v: k for k, v in STRING_TO_SUIT_MAPPING.items()}


class Values(enum.Enum):
    """A value from a typical western deck of cards."""

    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13


STRING_TO_VALUE_MAPPING = {
    "2": Values.TWO,
    "3": Values.THREE,
    "4": Values.FOUR,
    "5": Values.FIVE,
    "6": Values.SIX,
    "7": Values.SEVEN,
    "8": Values.EIGHT,
    "9": Values.NINE,
    "10": Values.TEN,
    "J": Values.JACK,
    "Q": Values.QUEEN,
    "K": Values.KING,
    "A": Values.ACE,
}
VALUE_TO_STRING_MAPPING = {v: k for k, v in STRING_TO_VALUE_MAPPING.items()}


@dataclass
class Card:
    """A playing card from a typical western deck of cards."""

    suit: Suits
    value: Values

    @staticmethod
    def from_string(string):
        """Parse a Card Object from it's string representation"""
        if len(string) != 2:
            raise ValueError(f"String: {string} must have 2 characters.")

        return Card(
            value=STRING_TO_VALUE_MAPPING[string[0]],
            suit=STRING_TO_SUIT_MAPPING[string[1]],
        )

    def __str__(self):
        return (
            f"{VALUE_TO_STRING_MAPPING[self.value]}{SUIT_TO_STRING_MAPPING[self.suit]}"
        )
