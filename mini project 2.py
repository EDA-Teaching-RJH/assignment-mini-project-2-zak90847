import random
import os
from validators import  validate_bet, validate_action

class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []
        