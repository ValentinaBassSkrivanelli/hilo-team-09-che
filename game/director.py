from game.croupier import Croupier
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.player_score = 300
        self.total_score = 0
        self.user_input = ""
        self.previous_card= 0

        #Call the class to obtain a card value.
        card = Croupier()
        card.give_number()
        self.card =  card.value

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
    def get_inputs(self):
        """Ask the user if the next number is Higher or Lower.

        Args:
            self (Director): An instance of Director.
        """ 
        #First Card
        self.previous_card = self.card
        print(f"The card is: {self.previous_card}")
        self.user_input = input("Higher or Lower? H/L: ")

        #Second card 
        card = Croupier()
        card.give_number()
        self.card =  card.value

        print(f"The next card is: {self.card}")
        print()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return