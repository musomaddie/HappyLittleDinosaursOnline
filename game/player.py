from game.hand_manager import Hand

class Player:
    """ The class that stores a player who is actually playing the game.

    Parameters:
        name                    str                 the name of the player
        dinosaur_character      DinosaurCharacter   the chosen dinosaur
        disaster_area           list[DisasterCards] the collected disaster
                                                    cards
        escape_route            int                 how far along the escape
                                                    route this player is
        hand                    Hand                the players hand
        account                 PlayerAccount       optionally link to a
                                                    created account.

    Methods:
        __init__(name)                      creates a new player object with
                                            the given name
        choose_dinosaur_character(dino)     assigns the given dinosaur
                                            character to this player
        draw(card)                          adds the given card to hand
        can_draw()              boolean     determines whether or not this
                                            player can draw more cards
    """

    def __init__(self, name):
        """ Creates a new player object.

        When the player is first created they have not yet had the chance to
        choose a dinosaur character or draw cards.

        Parameters:
            name        str         the chosen player name.

        Returns:
            Player      a player object with default values and the given
                        player name.
        """
        self.name = name
        self.dinosaur_character = None
        self.escape_route = 0
        self.disaster_area = []
        self.hand = Hand()
        self.account = None

    def choose_dinosaur_character(self, dino):
        """ Assigns the selected dinosaur to this player.

        Parameters:
            dino    DinosaurName    the name of the dinosaur to create
        """
        self.dinosaur_character = dino

    def draw(self, card):
        """ Adds the given card to this players hand.

        Parameters:
            card    Card    the card to add to hand
        """
        self.hand.add_card(card)

    def can_draw(self):
        """ Returns a boolean reflecting whether or not the player can draw
        more cards.

        Returns:
            boolean     true iff the player can draw more cards
        """
        return self.hand.need_cards()
