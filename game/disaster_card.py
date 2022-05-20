from game.card import Card
from game.db import get_db
from game.disaster_type import DisasterType

class DisasterCard(Card):
    """ For the disaster cards

    Parameters:
        disaster_type       DisasterType    the type of this disaster card
        description         str             the description of this disaster

    Methods:
        __init__(card_name, disaster_type, description)     creates a new
                                    disaster card with the given attributes

    Static Methods:
        load()          loads all the disaster cards from the database and
                        shuffles them.
    """
    def __init__(self, card_name, disaster_type, description):
        """ Creates a new DisasterCard object.

        Parameters:
            card_name       str             the name of the card
            disaster_type   DisasterType    the type of this disaster
            description     str             the description of this disaster
        """
        super().__init__(card_name)
        self.disaster_type = disaster_type
        self.description = description

    def __repr__(self):
        return f"{self.card_name} ({self.disaster_type.name})"

    @staticmethod
    def load():
        """ Loads shit
        """
        db = get_db()
        return [DisasterCard(card["card_name"],
                             DisasterType.find_value(card["disaster_type"]),
                             card["description"])
                for card in db.execute("SELECT * FROM disaster_cards;")
                for _ in range(card["quantity"])]
