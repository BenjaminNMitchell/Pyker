"""This module tests the parsing logic in poker.parsers.pokernow ."""

import unittest

from poker.model import player
from poker.model import actions
from poker.parsers.pokernow import parser


class ParserTests(unittest.TestCase):
    def test_get_players(self):

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
            player.Player(id_="9z1zzoqiIt", name="Ert"),
            player.Player(id_="TfZNpyIPhD", name="Suk"),
            player.Player(id_="PjBYO_8gbf", name="Russ"),
            player.Player(id_="bcp1N58-1M", name="Chon"),
            player.Player(id_="eSbnubU-KP", name="Benny"),
            player.Player(id_="izsy1Zibpi", name="Gargs"),
        }

        actual = parser.parse_players(test_player_lines)
        self.assertEqual(actual, expected)

    def test_get_actions(self):
        lines = [
            '"""Russ @ PjBYO_8gbf"" posts a small blind of 10",2021-01-09T18:14:11.908Z,161021605191410',
            '"""Chon @ bcp1N58-1M"" posts a big blind of 20",2021-01-09T18:14:11.908Z,161021605191411',
            '"""Russ @ PjBYO_8gbf"" posts a missing small blind of 10",2021-01-09T18:00:04.745Z,161021520474800',
            '"""Russ @ PjBYO_8gbf"" posts a missed big blind of 20",2021-01-09T18:00:04.745Z,161021520474800',
            '"""Benny @ eSbnubU-KP"" bets 75",2021-01-09T18:13:55.591Z,161021603559200',
            '"""Chon @ bcp1N58-1M"" calls 900",2021-01-09T18:16:22.467Z,161021618246800',
            '"""Suk @ TfZNpyIPhD"" raises to 900",2021-01-09T18:16:07.502Z,161021616750300',
            '"""Benny @ eSbnubU-KP"" folds",2021-01-09T18:14:13.944Z,161021605394700',
            '"""Russ @ PjBYO_8gbf"" checks",2021-01-09T18:15:01.151Z,161021610115200',
        ]

        expecteds = [
            actions.Post(
                player=player.Player(name="Russ", id_="PjBYO_8gbf"), amount=10
            ),
            actions.Post(
                player=player.Player(name="Chon", id_="bcp1N58-1M"), amount=20
            ),
            actions.Post(
                player=player.Player(name="Russ", id_="PjBYO_8gbf"), amount=10
            ),
            actions.Post(
                player=player.Player(name="Russ", id_="PjBYO_8gbf"), amount=20
            ),
            actions.Bet(
                player=player.Player(name="Benny", id_="eSbnubU-KP"), amount=75
            ),
            actions.Call(
                player=player.Player(name="Chon", id_="bcp1N58-1M"), amount=900
            ),
            actions.Raise(
                player=player.Player(name="Suk", id_="TfZNpyIPhD"), amount=900
            ),
            actions.Fold(player=player.Player(name="Benny", id_="eSbnubU-KP")),
            actions.Check(player=player.Player(name="Russ", id_="PjBYO_8gbf")),
        ]

        for line, expected in zip(lines, expecteds):
            with self.subTest(line=line, expected=expected):
                actual = parser.parse_action(line)
                self.assertEqual(actual, expected)
