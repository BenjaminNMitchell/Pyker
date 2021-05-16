from poker.encoders.json.street import StreetEncoder
import unittest

from poker.model import card, player, actions, street, hand, game
from poker.encoders.json.card import CardEncoder
from poker.encoders.json.player import PlayerEncoder
from poker.encoders.json.actions import (
    ActionEncoder,
    ActionWithAmountEncoder,
    ActionWithCardsEncoder,
)
from poker.encoders.json.hand import HandEncoder


class EncoderTests_JSON(unittest.TestCase):
    """Test JSON endcoder classes"""

    def setUp(self):
       self.card_model_QD = card.Card(value=card.Values.QUEEN, suit=card.Suits.DIAMONDS)
       self.card_json_QD = {"suit": "D", "value": "Q"}
    def test_serialize_card(self):

        self.assertEqual(self.card_json_QD, CardEncoder().default(self.card_model_QD))

    def test_serialize_player(self):

        model = player.Player(name="Oven", id_="jwf61y3XJg")
        expected = {"name": "Oven", "id_": "jwf61y3XJg"}

        self.assertEqual(expected, PlayerEncoder().default(model))

    def test_serialize_actions(self):

        p = player.Player(name="Oven", id_="jwf61y3XJg")

        check = actions.Check(player=p)
        expected_check = {
            "type": "check",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
        }
        fold = actions.Fold(player=p)
        expected_fold = {
            "type": "fold",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
        }

        self.assertEqual(expected_check, ActionEncoder().default(check))
        self.assertEqual(expected_fold, ActionEncoder().default(fold))

    def test_serialize_with_amount(self):

        p = player.Player(name="Oven", id_="jwf61y3XJg")
        v = 100
        awa_encoder = ActionWithAmountEncoder()

        bet = actions.Bet(player=p, amount=v)
        expected_bet = {
            "type": "bet",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        raise_ = actions.Raise(player=p, amount=v)
        expected_raise = {
            "type": "raise",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        call = actions.Call(player=p, amount=v)
        expected_call = {
            "type": "call",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        post = actions.Post(player=p, amount=v)
        expected_post = {
            "type": "post",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        collect = actions.Collect(player=p, amount=v)
        expected_collect = {
            "type": "collect",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        return_ = actions.Return(player=p, amount=v)
        expected_return = {
            "type": "return",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "amount": str(v),
        }

        self.assertDictEqual(expected_bet, awa_encoder.default(bet))
        self.assertDictEqual(expected_raise, awa_encoder.default(raise_))
        self.assertDictEqual(expected_call, awa_encoder.default(call))
        self.assertDictEqual(expected_post, awa_encoder.default(post))
        self.assertDictEqual(expected_collect, awa_encoder.default(collect))
        self.assertDictEqual(expected_return, awa_encoder.default(return_))

    def test_seralize_actions_with_cards(self):

        p = player.Player(name="Oven", id_="jwf61y3XJg")
        c = [card.Card(value="A", suit="D"), card.Card(value="A", suit="C")]

        model = actions.Show(player=p, cards=c)
        expected = {
            "type": "show",
            "player": {"name": "Oven", "id_": "jwf61y3XJg"},
            "cards": [{"suit": "D", "value": "A"}, {"suit": "C", "value": "A"}],
        }

        self.assertDictEqual(expected, ActionWithCardsEncoder().default(model))

    def test_seralize_street(self):

        self.maxDiff = None

        model = street.Street(
            actions=[
                actions.Fold(player=player.Player(name="Rus", id_="PjBYO_8gbf")),
                actions.Collect(
                    player=player.Player(name="Benny", id_="eSbnubU"), amount=10
                ),
                actions.Show(
                    player=player.Player(name="Rus", id_="PjBYO_8gbf"),
                    cards=[
                        card.Card(value="A", suit="D"),
                        card.Card(value="A", suit="C"),
                    ],
                ),
            ]
        )

        expected = {
            "actions": [
                {"type": "fold", "player": {"name": "Rus", "id_": "PjBYO_8gbf"}},
                {
                    "type": "collect",
                    "player": {"name": "Benny", "id_": "eSbnubU"},
                    "amount": "10",
                },
                {
                    "type": "show",
                    "player": {"name": "Rus", "id_": "PjBYO_8gbf"},
                    "cards": [{"suit": "D", "value": "A"}, {"suit": "C", "value": "A"}],
                },
            ]
        }

        self.assertDictEqual(expected, StreetEncoder().default(model))

    def test_serialize_short_hand(self):

        self.maxDiff = None

        model = hand.Hand(
            id=1,
            stacks = {player.Player(name="Rus", id_="PjBYO_8gbf"): 1000,
                      player.Player(name="Benny", id_="eSbnubU"): 1000},
            players =[
                player.Player(name="Rus", id_="PjBYO_8gbf"),
                player.Player(name="Benny", id_="eSbnubU")],
            our_cards = [card.Card(value="A", suit="D"),
                        card.Card(value="A", suit="C")],
            preflop=  street.Street(actions=[
                actions.Fold(player=player.Player(name="Rus", id_="PjBYO_8gbf")),
                actions.Collect(
                    player=player.Player(name="Benny", id_="eSbnubU"), amount=10),
                actions.Show(
                    player=player.Player(name="Rus", id_="PjBYO_8gbf"),
                    cards=[
                        card.Card(value="A", suit="D"),
                        card.Card(value="A", suit="C")],
                ),
            ]), 

            flop= [
                card.Card(value="K", suit="D"),
                card.Card(value="K", suit="C"),
                card.Card(value="K", suit='S')]
        ) 

        expected = {
            'id': '1',
            'players': [{"name": "Rus", "id_": "PjBYO_8gbf"},
                        {"name": "Benny", "id_": "eSbnubU"}],
            'our_cards': [{"suit": "D", "value": "A"}, {"suit": "C", "value": "A"}],
            'preflop': {'actions': [
                {"type": "fold", "player": {"name": "Rus", "id_": "PjBYO_8gbf"}},
                {
                    "type": "collect",
                    "player": {"name": "Benny", "id_": "eSbnubU"},
                    "amount": "10",
                },
                {
                    "type": "show",
                    "player": {"name": "Rus", "id_": "PjBYO_8gbf"},
                    "cards": [{"suit": "D", "value": "A"}, {"suit": "C", "value": "A"}],
                },]},
            'flop': [{'value': 'K', 'suit': 'D'},
            {'value': 'K', 'suit': 'C'},
            {'value': 'K', 'suit': 'S'}]
        }

        self.assertDictEqual(expected, HandEncoder().default(model))
        