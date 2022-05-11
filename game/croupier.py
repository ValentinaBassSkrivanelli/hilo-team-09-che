import random

class Croupier:
    """A Croupier is a person who draws or shuffles the cards in a game 
    including playing cards.
    
    Attributes:
        value (int) : a random number representing a card value 1-13
    """

    def __init__(self):
        """Creates the instance of a croupier"""

        self.value = 0
    
    def give_number(self):
        """draws a card (gets a random number for the card value)"""

        #generates a random value to assign to the value attribute
        self.value = random.randint(1, 13)
    

