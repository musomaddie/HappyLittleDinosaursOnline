from game.player import Player
from pytest import fixture

TEST_PLAYER_NAME = "Test Player"


@fixture
def player():
    return Player("TEST_PLAYER_NAME")

def test_init_player(player):
    assert player.name == "TEST_PLAYER_NAME"
    assert player.dinosaur_character is None
    assert player.escape_route == 0
    assert len(player.disaster_area) == 0
    assert player.hand is None
    assert player.account is None
