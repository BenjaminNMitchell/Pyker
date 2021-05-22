"""Collection of tests for model objects -> JSON"""
from unittest import TestCase

from test.encoders.json_fixtures import *
from test.model.model_fixtures import *

import pytest

from poker.encoders.json.player import PlayerEncoder
from poker.encoders.json.card import CardEncoder
from poker.encoders.json.actions import (
    ActionEncoder,
    ActionWithCardsEncoder,
    ActionWithAmountEncoder,
)
from poker.encoders.json.street import StreetEncoder
from poker.encoders.json.hand import HandEncoder


def test_serialize_card(ace_spades, ace_spades_json):
    """Test Card -> JSON"""
    TestCase().assertDictEqual(CardEncoder().default(ace_spades), ace_spades_json)


def test_serialize_player(rus_player, rus_player_json):
    """Test Player -> JSON"""
    TestCase().assertDictEqual(PlayerEncoder().default(rus_player), rus_player_json)


def test_serialize_base_actions(rus_check, rus_check_json):
    """Test Action -> JSON"""
    TestCase().assertDictEqual(ActionEncoder().default(rus_check), rus_check_json)


def test_serialize_bet(benny_bet, benny_bet_json):
    """Test ActionWithAmount -> JSON"""
    TestCase().assertDictEqual(
        ActionWithAmountEncoder().default(benny_bet), benny_bet_json
    )


def test_seralize_show(oven_show, oven_show_json):
    """Test ActionWithCards -> JSON"""
    TestCase().assertDictEqual(
        ActionWithCardsEncoder().default(oven_show), oven_show_json
    )


def test_serialize_street(street_check_fold, street_check_fold_json):
    """Test Street -> JSON"""
    TestCase().assertDictEqual(
        StreetEncoder().default(street_check_fold), street_check_fold_json
    )


def test_serialize_hand(hand_preflop, hand_preflop_json):
    """Test Hand -> JSON"""
    TestCase().assertDictEqual(HandEncoder().default(hand_preflop), hand_preflop_json)
