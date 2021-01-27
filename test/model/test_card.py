"""This module tests the parsing logic in card module."""

import unittest

from poker.model import card


class CardTests(unittest.TestCase):
    def test_from_string(self):

        test_cases = [
            {
                "string": "J♠",
                "card": card.Card(value=card.Values.JACK, suit=card.Suits.SPADES),
            },
            {
                "string": "Q♦",
                "card": card.Card(value=card.Values.QUEEN, suit=card.Suits.DIAMONDS),
            },
            {
                "string": "K♥",
                "card": card.Card(value=card.Values.KING, suit=card.Suits.HEARTS),
            },
            {
                "string": "A♣",
                "card": card.Card(value=card.Values.ACE, suit=card.Suits.CLUBS),
            },
        ]

        for test_case in test_cases:
            with self.subTest(string=test_case["string"], expected=test_case["card"]):

                string = test_case["string"]
                expected = test_case["card"]

                actual = card.Card.from_string(string)
                self.assertEqual(actual, expected)
