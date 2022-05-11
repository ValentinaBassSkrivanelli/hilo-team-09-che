import random

class Croupier:
    """A Croupier is a person who draws or shuffles the cards in a game 
    including playing cards.
    
    Attributes:
        value (int) : a random number representing a card value 1-13
    """

    def __init__(self):
        self.value = 0
    
    #(This function will give a random number between 1,13) 
    def give_number(self):
    
        card_number = random.randint(1,13)
        self.value = card_number