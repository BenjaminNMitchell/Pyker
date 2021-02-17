"""Tests for the filter module"""

import unittest


from poker.model.hand import Hand
from poker.model.player import Player
from poker.model.card import Card
from poker.model.actions import Fold, Raise, Post
from poker.model.street import Street
from poker.stats import filters


class FilterTests(unittest.TestCase):
    """Test the filter module."""

    def test_player_open_raised(self):

        russell = Player(name="Russell", id_="PjBYO_8gbf")
        max = Player(name="Max", id_="izsy1Zibpi")
        owen = Player(name="Owen", id_="jwf61y3XJg")
        ben = Player(name="Ben", id_="eSbnubU-KP")

        input_hand = Hand(
            players={
                russell,
                max,
                owen,
                ben,
            },
            our_cards=(Card.from_string("Q♠"), Card.from_string("3♠")),
            preflop=Street(
                actions=[
                    Post(player=russell, amount=5),
                    Post(player=max, amount=10),
                    Fold(player=owen),
                    Raise(player=ben, amount=30),
                ]
            ),
            flop=None,
            first=None,
            turn=None,
            second=None,
            river=None,
            third=None,
        )

        test_cases = [
            {
                "player": russell,
                "expected": False,
            },
            {
                "player": max,
                "expected": False,
            },
            {
                "player": owen,
                "expected": False,
            },
            {
                "player": ben,
                "expected": True,
            },
        ]

        for case in test_cases:
            with self.subTest(player=case["player"], expected=case["expected"]):
                actual = filters.player_open_raised(input_hand, player=case["player"])
                self.assertEqual(actual, case["expected"])
