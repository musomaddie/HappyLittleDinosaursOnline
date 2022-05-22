from game.db import _get_file_contents
from game.card import Card
from game.main_deck import MainDeck
from pytest import fixture

import pytest

@fixture
def main_deck(app):
    # I don't really care what the cards are, but I want an easy way to
    # differentiate where they initially were in the deck.
    main_deck = MainDeck(
        [Card(f"Card #{i + 1}") for i in range(35)]
    )
    return main_deck

def test_len(main_deck):
    assert len(main_deck) == 35

    main_deck.cards = []
    assert len(main_deck) == 0


def test_load(app):
    with app.app_context():
        deck = MainDeck.load()

    # Since this list is randomised I'm just going to check it's the expected
    # length.
    # If I wanted to be more thorough I could check that every expected card is
    # present the expected number of times but since this is already tested in
    # test_instant_card and test_point_card for the respective parts it feels
    # like overkill.
    expected_count = (
        sum([int(row[1]) for row in _get_file_contents("instant_cards")])
        + sum([int(row[1]) for row in _get_file_contents("point_cards")]))
    assert len(deck) == expected_count

def test_draw(main_deck):
    og_len = len(main_deck)
    card = main_deck.draw()
    assert card.card_name == "Card #1"
    assert len(main_deck) == og_len - 1

def test_draw_no_cards():
    main_deck = MainDeck([])
    with pytest.raises(ValueError) as e:
        main_deck.draw()

    assert str(e.value) == "Cannot draw from an empty deck"
