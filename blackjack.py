# **************BLACKJACK**************
# To play a hand of Blackjack the following steps must be followed:
# 1) Create a deck of 52 cards
# 2) Shuffle the deck
# 3) Ask the Player for their bet/define their chips
# 4) Make sure that the Player's bet does not exceed their available chips
# 5) Deal two cards to the Dealer and two cards to the Player
# 6) Show only one of the Dealer's cards, the other remains hidden
# 7) Show both of the Player's cards
# 8) Ask the Player if they wish to Hit, and take another card
# 9) If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# 10) If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11) Determine the winner and adjust the Player's chips accordingly
# 12) Ask the Player if they'd like to play again

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.deck = [] #Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card