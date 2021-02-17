"""This module tests the parsing logic in card module."""

import unittest

from poker.model import card


class CardTests(unittest.TestCase):
    """Test the card class."""

    def test_from_string(self):
        """Test from_string constructs cards correctly."""

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
            {
                "string": "10♠",
                "card": card.Card(value=card.Values.TEN, suit=card.Suits.SPADES),
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
            ValueError, "cannot parse card from string (.*)? invalid characters"
        ):
            _ = card.Card.from_string("K♥1")

    def test_str(self):
        """Test that str produces the correct string."""

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

    def test_is_sortable(self):
        """Test that cards are sortable."""

        cards = [
            card.Card(suit=card.Suits.CLUBS, value=card.Values.KING),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.ACE),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.SIX),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.SEVEN),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.QUEEN),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.THREE),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.TEN),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.EIGHT),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.FOUR),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.FIVE),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.TWO),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.JACK),
            card.Card(suit=card.Suits.CLUBS, value=card.Values.NINE),
        ]

        expected = [
            card.Card(value=card.Values.TWO, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.THREE, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.FOUR, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.FIVE, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.SIX, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.SEVEN, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.EIGHT, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.NINE, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.TEN, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.JACK, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.QUEEN, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.KING, suit=card.Suits.CLUBS),
            card.Card(value=card.Values.ACE, suit=card.Suits.CLUBS),
        ]

        actual = sorted(cards)
        self.assertEqual(actual, expected)

    def test_lt(self):
        """Test the less than method functions correctly."""

        ace_of_clubs = card.Card(value=card.Values.ACE, suit=card.Suits.CLUBS)
        ace_of_spades = card.Card(value=card.Values.ACE, suit=card.Suits.SPADES)
        two_of_clubs = card.Card(value=card.Values.TWO, suit=card.Suits.CLUBS)

        self.assertTrue(two_of_clubs < ace_of_clubs)
        self.assertTrue(two_of_clubs < ace_of_spades)

        self.assertFalse(ace_of_spades < ace_of_clubs)
        self.assertFalse(ace_of_clubs < ace_of_spades)
