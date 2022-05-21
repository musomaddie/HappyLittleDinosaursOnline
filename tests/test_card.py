from game.card import Card
from pytest import fixture

import pytest

TESTING_NAME = "Testing"

@fixture
def example_card():
    return Card(TESTING_NAME)

def test_init_(example_card):
    assert example_card.card_name == TESTING_NAME

def test_eq(example_card):
    matching_card = Card(TESTING_NAME)
    assert example_card == matching_card

    diff_card = Card("Different")
    assert example_card != diff_card

def test_eq_raises_error(example_card):
    with pytest.raises(ValueError) as e:
        example_card == "I am not a card"
    assert str(e.value) == ("'I am not a card' of type <class 'str'> cannot "
                            "be compared to Testing (Card)")

def test_repr(example_card):
    assert example_card.__repr__() == TESTING_NAME
