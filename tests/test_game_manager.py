from game.game_manager import GameManager
from pytest import mark

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


def test_init():
    gm = GameManager(["Alice", "Bob"])
    assert len(gm.players) == 2
    assert gm.main_deck is None
    assert gm.disaster_deck is None
