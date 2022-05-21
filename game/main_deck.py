from game.instant_card import InstantCard
from game.point_card import PointCard

import random

class MainDeck:
    """ Handles all operations around the Main Deck for a game. There should be
    exactly one of these for any given game. All interactions with cards in the
    main deck should be handled through this class.

    Parameters:
        cards   list[Card]      contains all the cards that can be drawn

    Methods:
        init()      creates a new deck.

    Static Methods:
        load()  MainDeck    loads all the cards from the database.
    """

    def __init__(self, cards):
        """ Creates a new MainDeck object. Should only be called as part of
        initial game setup.

        Parameters:
            cards   list[card]      all the cards that make up the deck for
                                    this game. Cards are either a Point Card or
                                    an Instant Card.
        """
        self.cards = cards

    @staticmethod
    def load():
        """ Loads and returns a new deck based on cards found in the database.

        Returns:
            MainDeck    the newly created deck
        """
        deck = PointCard.load() + InstantCard.load()
        random.shuffle(deck)
        return MainDeck(deck)
