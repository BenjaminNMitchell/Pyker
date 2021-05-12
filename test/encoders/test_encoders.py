import unittest
import json

from poker.model import card, player

from encoders.json.card import CardEncoder
from encoders.json.player import PlayerEncoder


class EncoderTests_JSON(unittest.TestCase):
    """Test JSON endcoder classes"""


    def test_serialize_card(self):
        
        model = card.Card(value=card.Values.QUEEN, suit=card.Suits.DIAMONDS)
        expected = {'suit': 'D', 'value': 'Q'}
        
        self.assertEqual(expected, CardEncoder().default(model))


    def test_serialize_player(self):

        model = player.Player(name="Oven", id_="jwf61y3XJg")
        expected = {'name': 'Oven', 'id_': "jwf61y3XJg"}

        self.assertEqual(expected, PlayerEncoder().default(model))