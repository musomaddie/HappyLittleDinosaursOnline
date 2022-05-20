from game.disaster_type import DisasterType
from pytest import mark

import pytest

@mark.parametrize(
    "value, disaster_type",
    [("Emotional", DisasterType.EMOTIONAL),
     ("emotional", DisasterType.EMOTIONAL),
     ("Natural", DisasterType.NATURAL),
     ("natural", DisasterType.NATURAL),
     ("predatory", DisasterType.PREDATORY),
     ("PreDATORY", DisasterType.PREDATORY)]
)
def test_find_value(value, disaster_type):
    assert DisasterType.find_value(value) == disaster_type

def test_find_value_raises():
    with pytest.raises(ValueError) as e:
        DisasterType.find_value("Testing")
    assert str(e.value) == "testing cannot be turned into a disaster type"
