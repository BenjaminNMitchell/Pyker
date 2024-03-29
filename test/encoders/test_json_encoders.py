"""Collection of tests for model objects -> JSON"""
# pylint: disable=redefined-outer-name, unused-import

from poker.encoders.json.exceptions import UnsupportedObjectToJSON
from unittest import TestCase

from test.encoders.json_fixtures import (
    ace_spades_json,
    rus_check_json,
    rus_player_json,
    benny_bet_json,
    oven_show_json,
    street_check_fold_json,
    hand_preflop_json,
    benny_player_json,
    rus_fold_json,
    oven_player_json,
    starting_stacks_rus_ben_oven_json,
)
from test.model.model_fixtures import (
    ace_spades,
    rus_check,
    rus_player,
    benny_bet,
    oven_show,
    street_check_fold,
    hand_preflop,
    benny_player,
    rus_fold,
    oven_player,
    starting_stacks_rus_ben_oven,
)

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
    TestCase().assertDictEqual(CardEncoder().encode(ace_spades), ace_spades_json)


def test_serialize_player(rus_player, rus_player_json):
    """Test Player -> JSON"""
    TestCase().assertDictEqual(PlayerEncoder().encode(rus_player), rus_player_json)


def test_serialize_base_actions(rus_check, rus_check_json):
    """Test Action -> JSON"""
    TestCase().assertDictEqual(ActionEncoder().encode(rus_check), rus_check_json)


def test_serialize_bet(benny_bet, benny_bet_json):
    """Test ActionWithAmount -> JSON"""
    TestCase().assertDictEqual(
        ActionWithAmountEncoder().encode(benny_bet), benny_bet_json
    )


def test_seralize_show(oven_show, oven_show_json):
    """Test ActionWithCards -> JSON"""
    TestCase().assertDictEqual(
        ActionWithCardsEncoder().encode(oven_show), oven_show_json
    )


def test_serialize_street(street_check_fold, street_check_fold_json):
    """Test Street -> JSON"""
    TestCase().assertDictEqual(
        StreetEncoder().encode(street_check_fold), street_check_fold_json
    )


def test_serialize_hand(hand_preflop, hand_preflop_json):
    """Test Hand -> JSON"""
    TestCase().assertDictEqual(HandEncoder().encode(hand_preflop), hand_preflop_json)


def type_mismatch_raises_exceptions():
    with pytest.raises(UnsupportedObjectToJSON):
        CardEncoder.encode("1")
