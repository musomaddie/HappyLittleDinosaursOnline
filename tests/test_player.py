from game.card import Card
from game.dinosaur import DinosaurCharacter, DinosaurName
from game.player import Player
from pytest import fixture
from unittest.mock import patch

TEST_PLAYER_NAME = "Test Player"
DINO = DinosaurCharacter.create_dinosaur(DinosaurName.STEGO)


@fixture
def player():
    return Player(TEST_PLAYER_NAME)

def test_init_player(player):
    assert player.name == TEST_PLAYER_NAME
    assert player.dinosaur_character is None
    assert player.escape_route == 0
    assert len(player.disaster_area) == 0
    assert len(player.hand.cards) == 0
    assert player.account is None

def test_repr(player):
    player.choose_dinosaur_character(DINO)
    assert player.__repr__() == "TEST PLAYER (DinosaurName.STEGO) []"

    player.hand.cards = [Card("Eg1"), Card("Eg2")]

def test_choose_dino(player):
    player.choose_dinosaur_character(DINO)
    assert player.dinosaur_character.name == DinosaurName.STEGO

@patch("game.player.Hand.add_card")
def test_draw(hand_mock, player):
    # Patching the call because I don't care how it actually works, it just
    # should be called.
    card = "Card 1"
    player.draw(card)
    assert hand_mock.called_with(card)

@patch("game.player.Hand.need_cards")
def test_can_draw(hand_mock, player):
    # Again patching because I don't need to test the implementation of the
    # hand method it should just be called
    player.can_draw()
    assert hand_mock.called_once()
