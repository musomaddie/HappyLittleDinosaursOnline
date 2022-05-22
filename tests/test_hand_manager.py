from game.hand_manager import Hand
from pytest import fixture

@fixture
def hand():
    return Hand()

def test_init(hand):
    assert len(hand) == 0

def test_repr(hand):
    assert hand.__repr__() == "[]"

    hand.cards = ["Hello", "World"]
    assert hand.__repr__() == "[Hello, World]"

def test_len(hand):
    assert len(hand) == 0
    [hand.add_card(i) for i in range(4)]
    assert len(hand) == 4

def test_add_card(hand):
    # TODO: change ot use actual cards
    hand.add_card("Card 1")
    assert len(hand.cards) == 1
    assert hand.cards[0] == "Card 1"

    hand.add_card("Card 2")
    assert len(hand.cards) == 2
    assert hand.cards[0] == "Card 1"
    assert hand.cards[1] == "Card 2"

def test_needs_cards(hand):
    assert hand.need_cards()
    for card in ["Card 1", "Card 2", "Card 3", "Card 4"]:
        hand.add_card(card)
        assert hand.need_cards()

    hand.add_card("Card 5")
    assert not hand.need_cards()
