class Card:
    """ Stores a card data for the game.

    Parameters:
        card_name   str         the name of the card

    Methods:
        __init__(card_name)     creates a new card with the given name

    Static Methods:
        load_cards()    loads both decks ready for game start.
    """
    def __init__(self, card_name):
        """ Creates a new card object with the given value.

        """
        self.card_name = card_name

    def __eq__(self, other):
        """ Checking equality between this card and another by comparing the
        card_name.

        Returns:
            bool        whether or not the two cards are the same, based on if
                        their card_names are the same.
        Raises:
            ValueError      if the provided object is not also a card.
        """
        if isinstance(other, Card):
            return self.card_name == other.card_name
        else:
            raise ValueError(f"'{other}' of type {type(other)} cannot be "
                             f"compared to {self.card_name} (Card)")
