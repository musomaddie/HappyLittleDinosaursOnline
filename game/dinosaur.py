from game.dinosaur_names import DinosaurName as name
from game.disaster_type import DisasterType as dt

class DinosaurCharacter:
    """ Stores the information relating to a particular dinosaur character.

    Properties:
        name                    DinosaurName        the name of this dinosaur.
        scoring_attributes      dict[DisasterType: int]     the point value
                                                    modifications that are used
                                                    during scoring.
        primary_colour          str                 the most prominent colour
                                                    in this dinosaur's image.

    Methods:
        __init__(dino_name, attributes, primary_colour)     creates a new dino
                                    object with the provided values.

    Static Methods:
        create_dinosaur(dino_name)      creates and returns a dinosaur
                                        character with properties that match
                                        the given name.
    """

    def __init__(self, dino_name, attributes, primary_colour):
        """ Only called by CLASS METHOD.
        Creates a new dinosaur character with the given values.

        Parameters:
            dino_name           DinosaurName    the name.
            attributes          dict[DisasterType: int]     the point values
                                                attributes of this dinosaur.
            primary_colour      string          the most prominent colour.

        Returns:
            DinosaurCharacter       the created dino character.
        """
        self.name = dino_name
        # TODO: consider making them ALL class values instead of a dict.
        self.scoring_attributes = attributes
        self.primary_colour = primary_colour

    @staticmethod
    def create_dinosaur(dinosaur_name):
        """ Creates and returns a DinosaurCharacter object with the values
        corresponding to the passed name.

        Parameters:
            dinosaur_name       DinosaurName    the name of the dinosaur

        Returns:
            DinosaurCharacter       the created dinosaur

        Raises:
            ValueError      if the dinosaur_name passed is not recognised.
        """
        attributes = {}
        colour = ""

        if dinosaur_name == name.NERVOUS_REX:
            attributes = {dt.PREDATORY: 1, dt.EMOTIONAL: -1}
            colour = "orange"
        elif dinosaur_name == name.BAD_LUCK_BRONTO:
            attributes = {dt.NATURAL: 1, dt.PREDATORY: -1}
            colour = "blue"
        elif dinosaur_name == name.CRY_CERATOPS:
            attributes = {dt.EMOTIONAL: 1, dt.NATURAL: -1}
            colour = "red"
        elif dinosaur_name == name.STEGO:
            attributes = {dt.METEOR: 1}
            colour = "green"
        else:  # Should never reach here.
            raise ValueError(
                f"{dinosaur_name} is not recognised as a dinosaur.")

        return DinosaurCharacter(dinosaur_name, attributes, colour)
