from game.instant_card import InstantCard, TimeOfPlay
from collections import defaultdict
from game.db import _get_file_contents
from pytest import fixture

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

def test_time_of_play_find_value():
    da = TimeOfPlay.DISASTER_ADD
    sco = TimeOfPlay.SCORING
    assert TimeOfPlay.find_value("Disaster Redirect") == da
    assert TimeOfPlay.find_value("Score Booster") == sco
    assert TimeOfPlay.find_value("Score Inversion") == sco
    assert TimeOfPlay.find_value("Score Snapper") == sco
    assert TimeOfPlay.find_value("Disaster Insurance") == da

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
