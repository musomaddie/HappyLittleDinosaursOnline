class Hand:
    """ Stores the hand of any given player. There should only be one of these
    per player.

    Parameters:
        list[Card]  cards       all the cards in this hand.

    Methods:
        __init__()      creates a new hand object (with no cards)
    """

    def __init__(self):
        """ Initialises a new empty hand. """
        self.cards = []
