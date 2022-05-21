from game.hand_manager import Hand
from pytest import fixture

@fixture
def hand():
    return Hand()

def test_init(hand):
    assert len(hand.cards) == 0
