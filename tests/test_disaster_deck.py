from game.card import Card
from game.db import _get_file_contents
from game.disaster_card import DisasterCard
from game.disaster_deck import DisasterDeck
from game.disaster_type import DisasterType
from pytest import fixture

@fixture
def deck():
    deck = DisasterDeck([DisasterCard(f"Card {i + 1}", DisasterType.METEOR, "")
                         for i in range(20)])
    return deck

def test_load(app):
    with app.app_context():
        deck = DisasterDeck.load()

    # Since this has been shuffled I'm just checking that it's the expected
    # length.
    expected_count = sum(
        [int(row[1]) for row in _get_file_contents("disaster_cards")])
    assert len(deck) == expected_count

def test_len(app):
    with app.app_context():
        deck = DisasterDeck([Card(str(i)) for i in range(35)])

    assert len(deck) == 35
    deck.cards = []
    assert len(deck) == 0

def test_draw(deck):
    old_deck_len = len(deck)
    card = deck.draw()
    assert card.card_name == "Card 1"
    assert len(deck) == old_deck_len - 1
