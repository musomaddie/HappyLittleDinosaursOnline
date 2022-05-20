from enum import Enum, auto
from game.card import Card
from game.db import get_db


class InstantCard(Card):
    """ Stores an instant card.

    Parameters:
        description     str         the description of the instant card.
        time_of_play    TimeOfPlay  when this card can be played.

    Methods:
        __init__(self, card_name)   creates a new instant card instance

    Static Methods:
        load()      loads all the instant cards from the database
    """
    def __init__(self, card_name, description):
        """ Creates a new intance of an instant card.

        Parameters:
            card_name   str     the name of the card
            description str     the description of the card.
        """
        super().__init__(card_name)
        self.description = description
        self.time_of_play = TimeOfPlay.find_value(card_name)

    def __repr__(self):
        return f"{self.card_name} (played {self.time_of_play.name})"

    @staticmethod
    def load():
        """ Loads all the cards from the database to be added to the deck at
        the start of the game. These cards are currently unshuffled.

        Returns:
            list[InstantCard] the newly created cards
        """
        db = get_db()
        # TODO: list comphrension??
        return [InstantCard(card["card_name"],
                            card["description"])
                for card in db.execute("SELECT * FROM instant_cards;")
                for _ in range(card["quantity"])]


class TimeOfPlay(Enum):
    """ A enum to store the two possible times to play an instant card.

    SCORING         this card can be played during the scoring of this round.
    DISASTER_ADD    this card can be played when the player would add a
                    disaster card to their disaster area.
    Methods:
        find_value(card_name)       assigns the
    """
    def find_value(card_name):
        """ Finds and returns the correct time of play depending on the card
        name.

        Parameters:
            card_name   str         the card name to find time of play for

        Returns:
            TimeOfPlay      the corresponding time of play

        Raises:
            ValueError      if the card_name cannot be recgonised
        """
        # Maintain alphabetic ordering.
        if card_name == "Disaster Insurance":
            return TimeOfPlay.DISASTER_ADD
        elif card_name == "Disaster Redirect":
            return TimeOfPlay.DISASTER_ADD
        elif card_name == "Score Booster":
            return TimeOfPlay.SCORING
        elif card_name == "Score Inversion":
            return TimeOfPlay.SCORING
        elif card_name == "Score Snapper":
            return TimeOfPlay.SCORING
        else:
            raise ValueError(f"{card_name} has no recognised time of play")

    SCORING = auto()
    DISASTER_ADD = auto()
