from game.instant_card import InstantCard, TimeOfPlay
from collections import defaultdict
from game.db import _get_file_contents
from pytest import fixture, mark

# import pytest

TESTING_NAME = "Score Booster"
TESTING_DESC = "testing description"
TESTING_TIME = TimeOfPlay.SCORING

@fixture
def card():
    return InstantCard(TESTING_NAME, TESTING_DESC)

def test_init(card):
    assert card.card_name == TESTING_NAME
    assert card.description == TESTING_DESC
    assert card.time_of_play == TESTING_TIME

@mark.parametrize(
    "value,top",
    [("Disaster Redirect", TimeOfPlay.DISASTER_ADD),
     ("Score Booster", TimeOfPlay.SCORING),
     ("Score Inversion", TimeOfPlay.SCORING),
     ("Score Snapper", TimeOfPlay.SCORING),
     ("Disaster Insurance", TimeOfPlay.DISASTER_ADD)]
)
def test_time_of_play_find_value(value, top):
    assert TimeOfPlay.find_value(value) == top

def test_repr(card):
    assert card.__repr__() == "Score Booster (played SCORING)"

def test_load(app):
    expected_cards = _get_file_contents("instant_cards")
    expected_count = sum([int(row[1]) for row in expected_cards])
    expected_card_counts = {row[0]: int(row[1]) for row in expected_cards}

    with app.app_context():
        cards = InstantCard.load()
    assert len(cards) == expected_count

    card_counts = defaultdict(int)
    for card in cards:
        card_counts[card.card_name] += 1

    for key in expected_card_counts:
        assert key in card_counts
        assert card_counts[key] == expected_card_counts[key]
