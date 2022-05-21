from game.game_manager import GameManager
from pytest import mark
from unittest.mock import patch

import pytest


@mark.parametrize(
    "players, error_message",
    [([], "Cannot start a game without any players"),
     (["Alice"], "Cannot start a game with only one player")]
)
def test_init_raises(players, error_message):
    with pytest.raises(ValueError) as e:
        GameManager(players)
    assert str(e.value) == error_message

@patch("game.game_manager.MainDeck.load")
@patch("game.game_manager.DisasterDeck.load")
def test_init(dd_load_mock, md_load_mock, app):
    with app.app_context():
        gm = GameManager(["Alice", "Bob"])
    assert len(gm.players) == 2
    assert md_load_mock.called
    assert dd_load_mock.called
