from game.main_deck import MainDeck
from game.db import _get_file_contents

def test_load(app):
    with app.app_context():
        cards = MainDeck.load()

    # Since this list is randomised I'm just going to check it's the expected
    # length.
    # If I wanted to be more thorough I could check that every expected card is
    # present the expected number of times but since this is already tested in
    # test_instant_card and test_point_card for the respective parts it feels
    # like overkill.
    expected_count = (
        sum([int(row[1]) for row in _get_file_contents("instant_cards")])
        + sum([int(row[1]) for row in _get_file_contents("point_cards")]))
    assert len(cards) == expected_count
