from game.dinosaur import DinosaurCharacter
from game.dinosaur_names import DinosaurName
from game.disaster_type import DisasterType as dt

import pytest

def test_init_dinosaur():
    dinosaur = DinosaurCharacter(
        DinosaurName.NERVOUS_REX, {"danger": 1}, "red")

    assert dinosaur.name == DinosaurName.NERVOUS_REX
    assert len(dinosaur.scoring_attributes) == 1
    assert "danger" in dinosaur.scoring_attributes
    assert dinosaur.scoring_attributes["danger"] == 1
    assert dinosaur.primary_colour == "red"

@pytest.mark.parametrize(
    "dino_name,expected_attr,expected_col",
    [(DinosaurName.NERVOUS_REX, {dt.PREDATORY: 1, dt.EMOTIONAL: -1}, "orange")
     ]
)
def test_create_dinosaur(dino_name, expected_attr, expected_col):
    dino = DinosaurCharacter.create_dinosaur(dino_name)

    assert dino.name == dino_name

    assert len(dino.scoring_attributes) == len(expected_attr)
    for actual, expected in zip(dino.scoring_attributes.keys(),
                                expected_attr.keys()):
        assert actual == expected
    for key in dino.scoring_attributes:
        assert dino.scoring_attributes[key] == expected_attr[key]

    assert dino.primary_colour == expected_col

def test_create_dinosaur_raises_error():
    with pytest.raises(ValueError) as e:
        DinosaurCharacter.create_dinosaur("Bob")
    assert str(e.value) == "Bob is not recognised as a dinosaur."
