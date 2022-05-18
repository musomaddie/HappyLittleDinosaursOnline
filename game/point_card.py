from game.card import Card
# I'm slightly worried that importing the get_db method might lead to some
# circular imports eventually. Considering accepting db as a variable.
from game.db import get_db

class PointCard(Card):
    """ Stores a point card.

    Parameters:
        value                           int         the point value of this
                                                    card
        special_effect                  boolean     whether this card has a
                                                    special effect
        special_effect_description      str         the description of the
                                                    special effect if it
                                                    exists, None otherwise.
    Methods:
        __init__(card_name, value, special_effect, special_effect_description)
                creates a new PointCard object.

    Static Methods:
        load()      loads all the cards from the database
    """
    def __init__(self, card_name, value, special_effect, special_eff_desc):
        super().__init__(card_name)
        self.value = value
        self.special_effect = special_effect
        self.special_effect_description = (special_eff_desc if special_effect
                                           else None)

    def __repr__(self):
        ending = " [e]" if self.special_effect else ""
        return f"{self.card_name} ({self.value}){ending}"

    @staticmethod
    def load():
        """ Loads all the cards from the database to form the deck at the start
        of a new game. These cards are currently unshuffled.

        Returns:
            list[PointCard]     the newly created cards.
        """
        db = get_db()
        card_list = db.execute("SELECT * FROM point_cards;")
        cards = []
        for card in card_list:
            for _ in range(card["quantity"]):
                cards.append(PointCard(card["card_name"],
                                       card["value"],
                                       card["special_effect"] == "TRUE",
                                       card["special_effect_description"]))
        return cards
