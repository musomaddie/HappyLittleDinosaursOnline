from game.main_deck import MainDeck
from game.disaster_deck import DisasterDeck

class GameManager:
    """ This class is responsible for managing the flow of the game. However,
    it should delegate responsibility reasonably to other managers. There
    should only ever be one of these per game.

    Parameters:
        players         list[Player]    all the players in this game
        main_deck       MainDeck        the main deck for this game
        disaster_deck   DisasterDeck    the disaster deck for this game

    Methods:
        __init__(players)      creates a new game manager for the given players
    """
    def __init__(self, players):
        """ Creates a new game manager when a game is started. All we know
        initially are the players as they have been decided in the waiting
        room where this method is called from.

        Parameters:
            players     list[Player]    all the players playing this game
                                        cannot be modified from this point
                                        onwards.

        Raises:
            ValueError      if there is 0 or 1 players
        """
        if len(players) <= 1:
            msg = "Cannot start a game with only one player"
            if len(players) == 0:
                msg = "Cannot start a game without any players"
            raise ValueError(msg)
        self.players = players
        self.main_deck = MainDeck.load()
        self.disaster_deck = DisasterDeck.load()
        self._deal_cards()

    def _deal_cards(self):
        """ A helper function responsible for adding cards to players hands
        from the main deck until everyone has five cards. Should not be called
        from outside this class.
        """
        players_to_draw = [player for player in self.players
                           if player.can_draw()]
        while len(players_to_draw) > 0:
            for player in players_to_draw:
                card = self.main_deck.draw()
                player.draw(card)
            players_to_draw = [player for player in self.players
                               if player.can_draw()]


    def play_round(self):
        """ Starts another round of the game. Returns a boolean which
        represents whether or not someone has won.

        Returns:
            boolean     true iff someone has won this game
        """
        # NOTE: my implementation plan is to implement the bare skeleton of the
        # round before going through and adding details.
        pass
