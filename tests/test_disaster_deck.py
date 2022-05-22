from game.card import Card
from game.db import _get_file_contents
from game.disaster_deck import DisasterDeck

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
