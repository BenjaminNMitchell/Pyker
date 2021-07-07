# pylint: disable=redefined-outer-name

"""JSON testing fixtures """

import pytest


@pytest.fixture
def rus_player_json():
    """Expected JSON for rus_player model-fixture"""
    return {"name": "Rus", "id_": "PjBYO_8gbf"}


@pytest.fixture
def oven_player_json():
    """Expected JSON for oven_player model-fixture"""
    return {"name": "Oven", "id_": "jwf61y3XJg"}


@pytest.fixture
def benny_player_json():
    """Expected JSON for benny_player model-fixture"""
    return {"name": "Benny", "id_": "eSbnubU"}


@pytest.fixture
def ace_spades_json():
    """Expected JSON for ace_spades model-fixture"""
    return {"value": "A", "suit": "S"}


@pytest.fixture
def rus_check_json(rus_player_json):
    """Expected JSON for rus_check model-fixture"""
    return {"type": "check", "player": rus_player_json}


@pytest.fixture
def rus_fold_json(rus_player_json):
    """Expected JSON for rus_fold model-fixture"""
    return {"type": "fold", "player": rus_player_json}


@pytest.fixture
def benny_bet_json(benny_player_json):
    """Expected JSON for benny_bet model-fixture"""
    return {"type": "bet", "player": benny_player_json, "amount": "30"}


@pytest.fixture
def oven_show_json(oven_player_json, ace_spades_json):
    """Expected JSON for oven_show model-fixture"""
    return {
        "type": "show",
        "player": oven_player_json,
        "cards": [ace_spades_json, ace_spades_json],
    }


@pytest.fixture
def street_check_fold_json(
    rus_check_json, benny_bet_json, rus_fold_json, oven_show_json
):
    """Expected JSON for street_check_fold model-fixture"""
    return {
        "actions": [
            rus_check_json,
            benny_bet_json,
            rus_fold_json,
            oven_show_json,
        ]
    }


@pytest.fixture
def starting_stacks_rus_ben_oven_json(rus_player, benny_player, oven_player):
    """Expected JSON for starting_stack_rus_ben_oven model-fixture"""
    return {
        rus_player.name.lower(): "1500",
        benny_player.name.lower(): "1500",
        oven_player.name.lower(): "1500",
    }


@pytest.fixture
def hand_preflop_json(
    street_check_fold_json,
    starting_stacks_rus_ben_oven_json,
    ace_spades_json,
    rus_player_json,
    benny_player_json,
    oven_player_json,
):
    """Expected JSON for hand_preflop_json model-fixture"""
    return {
        "id_": "0",
        "stacks": starting_stacks_rus_ben_oven_json,
        "players": [rus_player_json, benny_player_json, oven_player_json],
        "our_cards": [ace_spades_json, ace_spades_json],
        "preflop": street_check_fold_json,
    }
