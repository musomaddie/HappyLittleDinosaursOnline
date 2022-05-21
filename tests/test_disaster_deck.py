from game.disaster_deck import DisasterDeck
from game.db import _get_file_contents

def test_load(app):
    with app.app_context():
        deck = DisasterDeck.load()

    # Since this has been shuffled I'm just checking that it's the expected
    # length.
    expected_count = sum(
        [int(row[1]) for row in _get_file_contents("disaster_cards")])
    assert len(deck.cards) == expected_count
