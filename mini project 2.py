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
            for card in self .hand:
                if card in ['J','Q','K']:
                    score+= 10
                elif card == 'A':
                    aces += 1
                    score += 11
                else:
                    score += int(card)

            while score > 21 and aces:
                score -= 10
                aces -= 1
            return score

class Player(Participant):
    def __init__(self, name, balance=100):
        super().__init__(name)
        self.balance = balance

class Dealer(Participant):
    def __init__(self):
        super().__init__("Dealer")

def load_balance():
    if os.path.exists("save_games.txt"):
        with open("save_game.txt, "r") as f :
                  return int(f.read())
    return 100

def save_balance(balance)
    with open("save_game.txt, "w") as f:
              f.write(str(balance))

def play_game:
    balance = load_balance(
    player = Player ("User", balance)
    deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4
    random.shuffle(deck)

