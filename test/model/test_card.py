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
            # Alternate Suit Bindings
            {
                "string": "JS",
                "card": card.Card(value=card.Values.JACK, suit=card.Suits.SPADES),
            },
            {
                "string": "QD",
                "card": card.Card(value=card.Values.QUEEN, suit=card.Suits.DIAMONDS),
            },
            {
                "string": "KH",
                "card": card.Card(value=card.Values.KING, suit=card.Suits.HEARTS),
            },
            {
                "string": "AC",
                "card": card.Card(value=card.Values.ACE, suit=card.Suits.CLUBS),
            },
        ]

        for test_case in test_cases:
            with self.subTest(string=test_case["string"], expected=test_case["card"]):
                string = test_case["string"]
                expected = test_case["card"]
                actual = card.Card.from_string(string)
                self.assertEqual(actual, expected)

        with self.assertRaisesRegex(
            ValueError, "String: (.*)? must have 2 characters."
        ):
            _ = card.Card.from_string("K♥1")

    def test_str(self):

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
            with self.subTest(expected=test_case["string"], card=test_case["card"]):
                expected = test_case["string"]
                input_card = test_case["card"]
                actual = str(input_card)
                self.assertEqual(actual, expected)
