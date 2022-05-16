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
        self.hand = None
        self.account = None

    def choose_dinosaur_character(self, dino):
        """ Assigns the selected dinosaur to this player.

        Is a method so I can (later) do some constraint checking such as
        making sure that no-one has already chosen that dinosaur.
        """
        self.dinosaur_character = dino
