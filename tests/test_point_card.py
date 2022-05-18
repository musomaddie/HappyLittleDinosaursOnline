from collections import defaultdict
from game.db import _get_file_contents
from game.point_card import PointCard
from pytest import fixture

TESTING_NAME = "Testing"
TESTING_VALUE = 4
TESTING_SE_DESC = "I am a special effect!"

@fixture
def card_no_effect():
    return PointCard(TESTING_NAME, TESTING_VALUE, False, TESTING_SE_DESC)

@fixture
def card_with_effect():
    return PointCard(TESTING_NAME, TESTING_VALUE, True, TESTING_SE_DESC)

def test_init(card_no_effect, card_with_effect):
    assert card_no_effect.card_name == TESTING_NAME
    assert card_no_effect.value == TESTING_VALUE
    assert type(card_no_effect.value) is int
    assert not card_no_effect.special_effect
    assert card_no_effect.special_effect_description is None

    assert card_with_effect.card_name == TESTING_NAME
    assert card_with_effect.value == TESTING_VALUE
    assert card_with_effect.special_effect
    assert card_with_effect.special_effect_description == TESTING_SE_DESC

def test_repr(card_no_effect, card_with_effect):
    assert card_no_effect.__repr__() == f"{TESTING_NAME} ({TESTING_VALUE})"
    assert card_with_effect.__repr__() == (
        f"{TESTING_NAME} ({TESTING_VALUE}) [e]")

def test_load(app):
    expected_cards = _get_file_contents("point_cards")
    expected_count = sum([int(row[1]) for row in expected_cards])
    expected_card_counts = {row[0]: int(row[1]) for row in expected_cards}

    with app.app_context():
        cards = PointCard.load()
    assert len(cards) == expected_count

    card_counts = defaultdict(int)
    for card in cards:
        card_counts[card.card_name] += 1

    for key in expected_card_counts:
        assert key in card_counts
        assert card_counts[key] == expected_card_counts[key]

def test_cards_copied(app):
    # For my own piece of mind more than anything else.
    with app.app_context():
        cards = PointCard.load()
    c1 = cards[0]
    c2 = cards[1]
    assert c1 == c2

    c1.card_name = "something else"
    assert c1 != c2
