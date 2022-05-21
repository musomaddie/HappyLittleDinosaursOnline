class Hand:
    """ Stores the hand of any given player. There should only be one of these
    per player.

    Parameters:
        list[Card]  cards       all the cards in this hand.

    Methods:
        __init__()                  creates a new hand object (with no cards)
        need_cards()    boolean     returns true if the hand should contain
                                    more cards
        add_card(card)              adds the given card to the hand
    """

    def __init__(self):
        """ Initialises a new empty hand. """
        self.cards = []

    def need_cards(self):
        """ Returns true if the hand does not contain all five cards required
        to start a round.

        Returns:
            boolean         true iff there is less then 5 cards in the hand
        """
        return len(self.cards) < 5

    def add_card(self, card):
        """ Adds the given card to this hand.

        Parameters:
            card    Card        the card to add to hand. should only be either
                                a point card or an instant card as disaster
                                cards can't be added to the hand
        """
        # TODO: also call (and test) in player
        self.cards.append(card)
