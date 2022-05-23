from game.card import Card
from game.dinosaur import DinosaurName
from game.game_manager import GameManager
from game.main_deck import MainDeck
from game.player import Player
from pytest import mark, fixture
from unittest.mock import patch

import pytest

def _setup_players():
    alice = Player("Alice")
    alice.choose_dinosaur_character(DinosaurName.NERVOUS_REX)
    bob = Player("Bob")
    bob.choose_dinosaur_character(DinosaurName.BAD_LUCK_BRONTO)
    charlie = Player("Charlie")
    charlie.choose_dinosaur_character(DinosaurName.CRY_CERATOPS)
    dan = Player("Dan")
    dan.choose_dinosaur_character(DinosaurName.STEGO)
    return [alice, bob, charlie, dan]

@fixture
def game(app):
    # By the time the players are passed to the game they should have chosen
    # their dinosaur characters otherwise they wouldn't be able to leave the
    # waiting room.
    with app.app_context():
        # Patching so I don't have to read from the db unnecessarily
        with patch("game.game_manager.MainDeck.load"):
            with patch("game.game_manager.DisasterDeck.load"):
                return GameManager(_setup_players())

@mark.parametrize(
    "players, error_message",
    [([], "Cannot start a game without any players"),
     ([Player("Alice")], "Cannot start a game with only one player")]
)
def test_init_raises(players, error_message):
    with pytest.raises(ValueError) as e:
        GameManager(players)
    assert str(e.value) == error_message

@patch("game.game_manager.MainDeck.load")
@patch("game.game_manager.DisasterDeck.load")
def test_init_card_loads(dd_load_mock, md_load_mock, app):
    with app.app_context():
        game = GameManager([Player("Alice"), Player("Bob")])
    assert len(game.players) == 2
    assert game.active_disaster_card is None
    assert md_load_mock.called
    assert dd_load_mock.called

@patch("game.game_manager.MainDeck.load")
@patch("game.game_manager.DisasterDeck.load")
def test_init_deal_players(dd_load_mock, md_load_mock, app):
    md_load_mock.return_value = MainDeck(
        [Card(f"Card {i + 1}") for i in range(35)])
    with app.app_context():
        game = GameManager(
            [Player("Alice"), Player("Bob"), Player("Charlie"), Player("Dan")])

    assert len(game.main_deck) == 35 - (4 * 5)
    card_names = [[card.card_name for card in player.hand.cards]
                  for player in game.players]
    assert card_names[0] == ["Card 1", "Card 5", "Card 9",
                             "Card 13", "Card 17"]
    assert card_names[1] == ["Card 2", "Card 6", "Card 10",
                             "Card 14", "Card 18"]
    assert card_names[2] == ["Card 3", "Card 7", "Card 11",
                             "Card 15", "Card 19"]
    assert card_names[3] == ["Card 4", "Card 8", "Card 12",
                             "Card 16", "Card 20"]

###############################################################################
#                                                                             #
#                   DEAL CARDS                                                #
#                                                                             #
###############################################################################
@fixture
def gwc(app):
    with app.app_context():
        # Patching so I don't have to read from the db unnecessarily
        with patch("game.game_manager.MainDeck.load"):
            with patch("game.game_manager.DisasterDeck.load"):
                gm = GameManager(_setup_players())
                gm.main_deck = MainDeck(
                    [Card(f"Card #{i + 1}") for i in range(35)])
                return gm

def test_deal_cards_1_1(gwc):
    # Alice needs one card.
    alices_hand = [f"Existing Card {i + 1}" for i in range(4)]
    gwc.players[0].hand.cards = [Card(s) for s in alices_hand]

    og_deck_size = len(gwc.main_deck)
    og_top_card = gwc.main_deck.cards[0]

    gwc._deal_cards()

    for player in gwc.players:
        assert len(player.hand) == 5
    assert len(gwc.main_deck) == og_deck_size - 1
    assert og_top_card in gwc.players[0].hand.cards

def test_deal_cards_1_2(gwc):
    # Alice needs two cards
    alices_hand = [f"Existing card {i + 1}" for i in range(3)]
    gwc.players[0].hand.cards = [Card(s) for s in alices_hand]

    og_deck_size = len(gwc.main_deck)
    og_top_card = gwc.main_deck.cards[0]
    og_top_card_2 = gwc.main_deck.cards[1]

    gwc._deal_cards()

    for player in gwc.players:
        assert len(player.hand) == 5
    assert len(gwc.main_deck) == og_deck_size - 2
    assert og_top_card in gwc.players[0].hand.cards
    assert og_top_card_2 in gwc.players[0].hand.cards

def test_deal_cards_2_1(gwc):
    small_hands = [f"Existing card {i + 1}" for i in range(4)]
    gwc.players[0].hand.cards = [Card(s) for s in small_hands]
    gwc.players[1].hand.cards = [Card(s) for s in small_hands]

    og_deck_size = len(gwc.main_deck)
    og_top_card = gwc.main_deck.cards[0]
    og_top_card_2 = gwc.main_deck.cards[1]

    gwc._deal_cards()

    for player in gwc.players:
        assert len(player.hand) == 5
    assert len(gwc.main_deck) == og_deck_size - 2
    assert og_top_card in gwc.players[0].hand.cards
    assert og_top_card_2 in gwc.players[1].hand.cards

def test_deal_cards_1_2_3(gwc):
    gwc.players[0].hand.cards = [Card(f"Existing card {i + 1}")
                                 for i in range(4)]
    gwc.players[1].hand.cards = [Card(f"Existing card {i + 1}")
                                 for i in range(3)]
    gwc.players[2].hand.cards = [Card(f"Exisitng card {i + 1}")
                                 for i in range(2)]

    # Total of 6 cards
    og_deck_size = len(gwc.main_deck)
    og_tc_1 = gwc.main_deck.cards[0]
    og_tc_2 = gwc.main_deck.cards[1]
    og_tc_3 = gwc.main_deck.cards[2]
    og_tc_4 = gwc.main_deck.cards[3]
    og_tc_5 = gwc.main_deck.cards[4]
    og_tc_6 = gwc.main_deck.cards[5]

    gwc._deal_cards()

    for player in gwc.players:
        assert len(player.hand) == 5
    assert len(gwc.main_deck) == og_deck_size - 6
    assert og_tc_1 in gwc.players[0].hand.cards
    assert og_tc_2 in gwc.players[1].hand.cards
    assert og_tc_3 in gwc.players[2].hand.cards
    assert og_tc_4 in gwc.players[1].hand.cards
    assert og_tc_5 in gwc.players[2].hand.cards
    assert og_tc_6 in gwc.players[2].hand.cards

    gwc._deal_cards()

def test_deal_cards_none(gwc):
    og_deck_size = len(gwc.main_deck)
    gwc._deal_cards()
    for player in gwc.players:
        assert len(player.hand) == 5
    assert len(gwc.main_deck) == og_deck_size
