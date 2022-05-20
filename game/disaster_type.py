from enum import Enum, auto

class DisasterType(Enum):
    def find_value(s):
        s = s.lower()
        if s == "emotional":
            return DisasterType.EMOTIONAL
        elif s == "natural":
            return DisasterType.NATURAL
        elif s == "predatory":
            return DisasterType.PREDATORY
        elif s == "meteor":
            return DisasterType.METEOR
        else:  # Should never reach this
            raise ValueError(f"{s} cannot be turned into a disaster type")

    EMOTIONAL = auto()
    NATURAL = auto()
    PREDATORY = auto()
    METEOR = auto()
