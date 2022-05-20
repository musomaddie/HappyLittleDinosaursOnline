from collections import defaultdict
from game.db import _get_file_contents
from game.disaster_card import DisasterCard
from game.disaster_type import DisasterType
from pytest import fixture

TESTING_NAME = "Testing"
TESTING_DT = DisasterType.METEOR
TESTING_DESC = "RAWR! I am a meteor"

@fixture
def card():
    return DisasterCard(TESTING_NAME, TESTING_DT, TESTING_DESC)

def test_init(card):
    assert card.card_name == TESTING_NAME
    assert card.disaster_type == TESTING_DT
    assert card.description == TESTING_DESC

def test_repr(card):
    assert card.__repr__() == "Testing (METEOR)"

def test_load(app):
    expected_cards = _get_file_contents("disaster_cards")
    expected_count = sum([int(row[1]) for row in expected_cards])
    expected_card_counts = {row[0]: int(row[1]) for row in expected_cards}

    with app.app_context():
        cards = DisasterCard.load()

    assert len(cards) == expected_count

    card_counts = defaultdict(int)
    for card in cards:
        card_counts[card.card_name] += 1

    for key in expected_card_counts:
        assert key in card_counts
        assert card_counts[key] == expected_card_counts[key]
