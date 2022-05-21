from game.disaster_card import DisasterCard

import random

class DisasterDeck:
    """ Handles all operations around the Disaster Deck for a game. There
    should be exactly one of these for any given game. All interactions with
    cards in the disaster deck should be handled through this class.

    Parameters:
        cards   list[DisasterCard]  contains all the cards in the disaster deck

    Methods:
        init()      creates a new deck

    Static Methods:
        load()      loads all the cards from the database ready for game start
    """
    def __init__(self, cards):
        """ Creates a new DisasterDeck object. Should only be called as part
        of initial game setup.

        Parameters:
            cards   list[DisasterCard]      all the cards that make up the
                                            disaster deck for this game
        """
        self.cards = cards

    @staticmethod
    def load():
        """ Loads and returns a new deck containing shuffled cards from the
        database. Should only be called during initial game set up.

        Returns:
            DisasterDeck    the newly created disaster deck object
        """
        deck = DisasterCard.load()
        random.shuffle(deck)
        return DisasterDeck(deck)
