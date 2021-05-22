"""Poker model fixtures"""

import pytest
from poker.model import card, player, hand, street, actions


@pytest.fixture
def rus_player():
    """Sample Player"""
    return player.Player(name="Rus", id_="PjBYO_8gbf")


@pytest.fixture
def oven_player():
    """Sample Player"""
    return player.Player(name="Oven", id_="jwf61y3XJg")


@pytest.fixture
def benny_player():
    """Sample Player"""
    return player.Player(name="Benny", id_="eSbnubU")


@pytest.fixture
def ace_spades():
    """Sample Card"""
    return card.Card(suit="S", value="A")


@pytest.fixture
def rus_check(rus_player):
    """Sample Basic Action"""
    return actions.Check(player=rus_player)


@pytest.fixture
def rus_fold(rus_player):
    """Sample Basic Action"""
    return actions.Fold(player=rus_player)


@pytest.fixture
def benny_bet(benny_player):
    """Sample Action with amount"""
    return actions.Bet(player=benny_player, amount=30)


@pytest.fixture
def oven_show(oven_player, ace_spades):
    """Sample Action with 2 cards"""
    return actions.Show(player=oven_player, cards=[ace_spades, ace_spades])


@pytest.fixture
def street_check_fold(rus_check, benny_bet, rus_fold, oven_show):
    """Sample Street (Check -> Bet -> Fold)"""
    return street.Street(
        actions=[
            rus_check,
            benny_bet,
            rus_fold,
            oven_show,
        ]
    )


@pytest.fixture
def starting_stacks_rus_ben_oven(rus_player, benny_player, oven_player):
    """Sample chip stacks. 3 * (player -> int)"""
    return {rus_player: 1500, benny_player: 1500, oven_player: 1500}


@pytest.fixture
def hand_preflop(
    street_check_fold,
    starting_stacks_rus_ben_oven,
    rus_player,
    benny_player,
    oven_player,
    ace_spades,
):
    """Sample Hand (Ends before flop)"""
    return hand.Hand(
        id_=0,
        stacks=starting_stacks_rus_ben_oven,
        players=[rus_player, benny_player, oven_player],
        our_cards=[ace_spades, ace_spades],
        preflop=street_check_fold,
        flop=None,
        first=None,
        turn=None,
        second=None,
        river=None,
        third=None,
    )
