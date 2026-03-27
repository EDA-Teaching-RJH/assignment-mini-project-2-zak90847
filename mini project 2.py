import random
import os
from validators import  validate_bet, validate_action

class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []

        def add_card(self, card):
            self.hand.append(card)
        
        def get_score(self):
            score = 0
            aces = 0
            