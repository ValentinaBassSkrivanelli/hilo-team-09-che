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
        card (int): the value of a card
        score (int): the score at the end of the score
        total_score (int): the total score of the player
        user_input (str): input by the user (h/l) 
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

        print("Game Over")
        print("Thanks for Playing!")

    def get_inputs(self):
        """Ask the user if they believe is High or Low.

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
        
        die = die.calculate()
            self.value = random.randint(1, 13)
            self.points = 100 if self.value > first_card and user_input == "h" 100 else self.value < first_card and user_input == "l" else -75

            self.score += die.points
            self.total_score += self.score


    def do_outputs(self):
        """Displays the next card value. Also asks the player if they want 
        to play again. 

        Args:
            self (Director): An instance of Director.
        """

        #if false, the game is over 
        if not self.is_playing:
            print("Game Over")
            print("Thanks for Playing!")
            return 
        
        #print the score
        print(f"Score: {self.score}")

        #if the score is greater than zero, ask if the user
        #wants to play again
        if self.score > 0:
            token = 1
            while token == 1:
                retry = input("Play again? (Y/N): ")
                
                if retry.lower() == "y":
                    self.is_playing = True
                    token = 0

                elif retry.lower() == "n":
                    self.is_playing = False
                    token = 0
                    print("Game Over")
                    print("Thanks for Playing!")

                else:
                    print("please insert a valid letter.")

        else:
            self.is_playing = False
        print()
