import re
import random

class Participant:
    def __init(self,name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)