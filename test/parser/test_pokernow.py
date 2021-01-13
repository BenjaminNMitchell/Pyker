"""This module tests the parsing logic in poker.parsers.pokernow ."""

import unittest

from poker.model import player
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
