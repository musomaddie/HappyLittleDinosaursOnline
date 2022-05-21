from game.dinosaur import DinosaurName
from game.game_manager import GameManager
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
    assert md_load_mock.called
    assert dd_load_mock.called
