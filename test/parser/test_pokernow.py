"""This module tests the parsing logic in poker.parsers.pokernow ."""

import unittest

from poker.model.actions import (
    Bet,
    Call,
    Fold,
    Check,
    Post,
    Raise,
    Collect,
    Return,
    Show,
)
from poker.model.player import Player
from poker.model.hand import Hand
from poker.model.street import Street
from poker.model.card import Card
from poker.parsers.pokernow import parser


class ParserTests(unittest.TestCase):
    """Tests for the poker now parser."""

    def test_get_players(self):
        """Test that get_players correctly parses the players line."""

        test_player_lines = (
            '"Player stacks: '
            '#1 ""Ert @ 9z1zzoqiIt"" (2000) | '
            '#2 ""`~!@#$%^& @ 9z1zzoqiIt"" (2000) | '
            '#3 ""Paulie. D @ TfZNpyIPhD"" (2000) | '
            '#4 ""Russ @ PjBYO_8gbf"" (2000) | '
            '#6 ""Chon @ bcp1N58-1M"" (2000) | '
            '#8 ""Benny @ eSbnubU-KP"" (2000) | '
            '#9 ""Gargs @ izsy1Zibpi"" (2000)"'
            ",2021-01-09T18:13:11.491Z,161021599150607"
        )

        expected = {
            Player(id_="9z1zzoqiIt", name="Ert"),
            Player(id_="9z1zzoqiIt", name="`~!@#$%^&"),
            Player(id_="TfZNpyIPhD", name="Paulie. D"),
            Player(id_="PjBYO_8gbf", name="Russ"),
            Player(id_="bcp1N58-1M", name="Chon"),
            Player(id_="eSbnubU-KP", name="Benny"),
            Player(id_="izsy1Zibpi", name="Gargs"),
        }

        actual, _ = parser.parse_players(test_player_lines)
        self.assertEqual(actual, expected)

    def test_get_stacks(self):
        """Tests that player names are parsed along with their hand starting stacks"""

        test_player_lines = (
            '"Player stacks: '
            '#1 ""Ert @ 9z1zzoqiIt"" (2000) | '
            '#3 ""Suk @ TfZNpyIPhD"" (2000) | '
            '#4 ""Russ @ PjBYO_8gbf"" (2000) | '
            '#6 ""Chon @ bcp1N58-1M"" (2000) | '
            '#8 ""Benny @ eSbnubU-KP"" (2000) | '
            '#9 ""Gargs @ izsy1Zibpi"" (2000)"'
            ",2021-01-09T18:13:11.491Z,161021599150607"
        )

        expected = {
            Player(id_="9z1zzoqiIt", name="Ert"): 2000,
            Player(id_="TfZNpyIPhD", name="Suk"): 2000,
            Player(id_="PjBYO_8gbf", name="Russ"): 2000,
            Player(id_="bcp1N58-1M", name="Chon"): 2000,
            Player(id_="eSbnubU-KP", name="Benny"): 2000,
            Player(id_="izsy1Zibpi", name="Gargs"): 2000,
        }

        _, actual = parser.parse_players(test_player_lines)

        self.assertEqual(actual, expected)

    def test_get_actions(self):
        """Test that get_actions correctly parses actions."""

        lines = [
            '"""Russ @ PjBYO_8gbf"" posts a small blind of 10"'
            ",2021-01-09T18:14:11.908Z,161021605191410",
            '"""Chon @ bcp1N58-1M"" posts a big blind of 20"'
            ",2021-01-09T18:14:11.908Z,161021605191411",
            '"""Russ @ PjBYO_8gbf"" posts a missing small blind of 10"'
            ",2021-01-09T18:00:04.745Z,161021520474800",
            '"""Russ @ PjBYO_8gbf"" posts a missed big blind of 20"'
            ",2021-01-09T18:00:04.745Z,161021520474800",
            '"""Benny @ eSbnubU-KP"" bets 75",2021-01-09T18:13:55.591Z,161021603559200',
            '"""Chon @ bcp1N58-1M"" calls 900",2021-01-09T18:16:22.467Z,161021618246800',
            '"""Suk @ TfZNpyIPhD"" raises to 900",2021-01-09T18:16:07.502Z,161021616750300',
            '"""Benny @ eSbnubU-KP"" folds",2021-01-09T18:14:13.944Z,161021605394700',
            '"""Russ @ PjBYO_8gbf"" checks",2021-01-09T18:15:01.151Z,161021610115200',
        ]

        expecteds = [
            Post(player=Player(name="Russ", id_="PjBYO_8gbf"), amount=10),
            Post(player=Player(name="Chon", id_="bcp1N58-1M"), amount=20),
            Post(player=Player(name="Russ", id_="PjBYO_8gbf"), amount=10),
            Post(player=Player(name="Russ", id_="PjBYO_8gbf"), amount=20),
            Bet(player=Player(name="Benny", id_="eSbnubU-KP"), amount=75),
            Call(player=Player(name="Chon", id_="bcp1N58-1M"), amount=900),
            Raise(player=Player(name="Suk", id_="TfZNpyIPhD"), amount=900),
            Fold(player=Player(name="Benny", id_="eSbnubU-KP")),
            Check(player=Player(name="Russ", id_="PjBYO_8gbf")),
        ]

        for line, expected in zip(lines, expecteds):
            with self.subTest(line=line, expected=expected):
                actual = parser.parse_action(line)
                self.assertEqual(actual, expected)

    def test_parse_hand(self):
        """Test that parse_hand correctly parses the hand."""

        hand_lines = [
            '"-- starting hand #6  (No Limit Texas Hold\'em) (dealer: ""Eddy KGB @ _7OU6FzFZP"")'
            ' --",2020-12-17T00:44:19.590Z,160816585959100',
            '"Player stacks: #1 ""MOP @ jwf61y3XJg"" (1060) | #4 ""rus @ PjBYO_8gbf"" (971) |'
            ' #6 ""Eddy KGB @ _7OU6FzFZP"" (1025) | #7 ""Ben @ eSbnubU-KP"" (1057) | #8'
            ' ""Max @ izsy1Zibpi"" (887)",2020-12-17T00:44:19.590Z,160816585959101',
            '"Your hand is Q♠, 3♠",2020-12-17T00:44:19.590Z,160816585959105',
            '"""Ben @ eSbnubU-KP"" posts a small blind of 5",'
            "2020-12-17T00:44:19.590Z,160816585959107",
            '"""Max @ izsy1Zibpi"" posts a big blind of 10",'
            "2020-12-17T00:44:19.590Z,160816585959108",
            '"""MOP @ jwf61y3XJg"" folds",2020-12-17T00:44:22.437Z,160816586243800',
            '"""rus @ PjBYO_8gbf"" calls 10",2020-12-17T00:44:25.141Z,160816586514100',
            '"""Eddy KGB @ _7OU6FzFZP"" calls 10",2020-12-17T00:44:28.601Z,160816586860200',
            '"""Ben @ eSbnubU-KP"" calls 10",2020-12-17T00:44:31.296Z,160816587129700',
            '"""Max @ izsy1Zibpi"" checks",2020-12-17T00:44:32.791Z,160816587279100',
            '"flop:  [J♠, 10♥, 6♥]",2020-12-17T00:44:33.595Z,160816587359600',
            '"""Ben @ eSbnubU-KP"" checks",2020-12-17T00:44:40.619Z,160816588062000',
            '"""Max @ izsy1Zibpi"" checks",2020-12-17T00:44:41.477Z,160816588147800',
            '"""rus @ PjBYO_8gbf"" checks",2020-12-17T00:44:44.131Z,160816588413200',
            '"""Eddy KGB @ _7OU6FzFZP"" checks",2020-12-17T00:44:46.017Z,160816588601700',
            '"turn: J♠, 10♥, 6♥ [Q♦]",2020-12-17T00:44:46.823Z,160816588682400',
            '"""Ben @ eSbnubU-KP"" checks",2020-12-17T00:44:50.123Z,160816589012400',
            '"""Max @ izsy1Zibpi"" checks",2020-12-17T00:44:57.859Z,160816589786000',
            '"""rus @ PjBYO_8gbf"" checks",2020-12-17T00:44:59.202Z,160816589920300',
            '"""Eddy KGB @ _7OU6FzFZP"" checks",2020-12-17T00:45:01.677Z,160816590167800',
            '"river: J♠, 10♥, 6♥, Q♦ [3♣]",2020-12-17T00:45:02.499Z,160816590250400',
            '"""Ben @ eSbnubU-KP"" bets 30",2020-12-17T00:45:08.970Z,160816590897100',
            '"""Max @ izsy1Zibpi"" calls 30",2020-12-17T00:45:10.705Z,160816591070600',
            '"""rus @ PjBYO_8gbf"" calls 30",2020-12-17T00:45:25.416Z,160816592541700',
            '"""Eddy KGB @ _7OU6FzFZP"" folds",2020-12-17T00:45:26.287Z,160816592628700',
            '"""Ben @ eSbnubU-KP"" shows a Q♠, 3♠.",2020-12-17T00:45:27.095Z,160816592709700',
            '"""Ben @ eSbnubU-KP"" collected 130 from pot with Two Pair, Q\'s & 3\'s'
            ' (combination: Q♠, Q♦, 3♠, 3♣, J♠)",2020-12-17T00:45:27.095Z,160816592709701',
            '"-- ending hand #6 --",2020-12-17T00:45:27.095Z,160816592709702',
        ]

        expected_hand = Hand(
            id=6,
            players={
                Player(name="Ben", id_="eSbnubU-KP"),
                Player(name="Eddy KGB", id_="_7OU6FzFZP"),
                Player(name="MOP", id_="jwf61y3XJg"),
                Player(name="Max", id_="izsy1Zibpi"),
                Player(name="rus", id_="PjBYO_8gbf"),
            },
            stacks={
                Player(name="MOP", id_="jwf61y3XJg"): 1060,
                Player(name="rus", id_="PjBYO_8gbf"): 971,
                Player(name="Eddy KGB", id_="_7OU6FzFZP"): 1025,
                Player(name="Ben", id_="eSbnubU-KP"): 1057,
                Player(name="Max", id_="izsy1Zibpi"): 887,
            },
            our_cards=(Card.from_string("Q♠"), Card.from_string("3♠")),
            preflop=Street(
                actions=[
                    Post(player=Player(name="Ben", id_="eSbnubU-KP"), amount=5),
                    Post(player=Player(name="Max", id_="izsy1Zibpi"), amount=10),
                    Fold(player=Player(name="MOP", id_="jwf61y3XJg")),
                    Call(player=Player(name="rus", id_="PjBYO_8gbf"), amount=10),
                    Call(player=Player(name="Eddy KGB", id_="_7OU6FzFZP"), amount=10),
                    Call(player=Player(name="Ben", id_="eSbnubU-KP"), amount=10),
                    Check(player=Player(name="Max", id_="izsy1Zibpi")),
                ]
            ),
            flop=[
                Card.from_string("J♠"),
                Card.from_string("10♥"),
                Card.from_string("6♥"),
            ],
            first=Street(
                actions=[
                    Check(player=Player(name="Ben", id_="eSbnubU-KP")),
                    Check(player=Player(name="Max", id_="izsy1Zibpi")),
                    Check(player=Player(name="rus", id_="PjBYO_8gbf")),
                    Check(player=Player(name="Eddy KGB", id_="_7OU6FzFZP")),
                ]
            ),
            turn=[Card.from_string("Q♦")],
            second=Street(
                actions=[
                    Check(player=Player(name="Ben", id_="eSbnubU-KP")),
                    Check(player=Player(name="Max", id_="izsy1Zibpi")),
                    Check(player=Player(name="rus", id_="PjBYO_8gbf")),
                    Check(player=Player(name="Eddy KGB", id_="_7OU6FzFZP")),
                ]
            ),
            river=[Card.from_string("3♣")],
            third=Street(
                actions=[
                    Bet(player=Player(name="Ben", id_="eSbnubU-KP"), amount=30),
                    Call(player=Player(name="Max", id_="izsy1Zibpi"), amount=30),
                    Call(player=Player(name="rus", id_="PjBYO_8gbf"), amount=30),
                    Fold(player=Player(name="Eddy KGB", id_="_7OU6FzFZP")),
                    Show(
                        player=Player("Ben", id_="eSbnubU-KP"),
                        cards=(Card.from_string("Q♠"), Card.from_string("3♠")),
                    ),
                    Collect(player=Player(name="Ben", id_="eSbnubU-KP"), amount=130),
                ]
            ),
        )

        actual_hand = parser.parse_hand(hand_lines=hand_lines)

        self.assertCountEqual(actual_hand.players, expected_hand.players)
        self.assertEqual(actual_hand.stacks, expected_hand.stacks)
        self.assertEqual(actual_hand.preflop, expected_hand.preflop)
        self.assertEqual(actual_hand.flop, expected_hand.flop)
        self.assertEqual(actual_hand.first, expected_hand.first)
        self.assertEqual(actual_hand.turn, expected_hand.turn)
        self.assertEqual(actual_hand.second, expected_hand.second)
        self.assertEqual(actual_hand.river, expected_hand.river)
        self.assertEqual(actual_hand.third, expected_hand.third)

    def test_parse_straddle_action(self):
        """Test that test_parse_straddle_action correctly constructs straddles."""

        line = '"""Benny @ jzQ-urBlJX"" posts a straddle of 20",2021-02-11T02:41:46.355Z,161301130635712'
        actual = parser.parse_action(line)
        expected = Post(player=Player(name="Benny", id_="jzQ-urBlJX"), amount=20)
        self.assertEqual(actual, expected)

    def test_parse_return_action(self):
        """Test that test_parse_return_action correctly builds the Return"""

        line = '"Uncalled bet of 66 returned to ""Oven @ hogtf8AO2o""",2021-02-11T02:41:46.355Z,161301130635712'
        actual = parser.parse_action(line)
        expected = Return(player=Player(name="Oven", id_="hogtf8AO2o"), amount=66)
        self.assertEqual(actual, expected)

    def test_parse_shows_with_cards(self):
        """Test that parse_show_with_cards correctly extracts the card information."""

        line = '"""Gargs @ izsy1Zibpi"" shows a A♠, A♣.",2021-02-11T02:41:46.355Z,161301130635712'
        actual = parser.parse_action(line)
        expected = Show(
            player=Player(name="Gargs", id_="izsy1Zibpi"),
            cards=(Card.from_string("A♠"), Card.from_string("A♣")),
        )
        self.assertEqual(actual, expected)
