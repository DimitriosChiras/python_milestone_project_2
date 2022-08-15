## 1) Have a deck, 2) shuffle it, 3) split it in two equal halves, 4) both players
## reveal simultaneously their top card and compare it, 4i) the card that has the
## higher ranking wins and the player that wins the matchup takes both cards and 
## puts them in their deck, 4ii) if the cards have the exact same value then it's WAR
## 5) WAR: both players take 3 cards face down and a last one face up: 5i) same as before
## the card with the higher ranking wins, 5ii) in case of another WAR, repeat,
## 5iii) if a player runs out of cards during war, then they lose.
## 6) WIN CONDITION: one player has gathered all of the cards

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Card class: 
# It should 1) Understand the suit of the card (hearts, diamonds clubs), 2) rank (1,2,3....king)
# and 3) an easy-to-use integer value corresponding to that rank so that we can compare 
# later on 2 instances of the card class and decide which card has the higher value

class Card:
# When someone creates an instance of the card they should provide the suit 
# and rank of the card (the value we don't need as it will be calcullated from a dictionary)
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit #Assumes that rank and suit passed in are strings

# Deck class:
# It should 1) instantiate a new deck (create all 52 card objects AND hold them as a LIST of card objects)
# 2) shuffle a deck through the shuffle() function from the random library and 3) deal cards from
# the Deck object using the Pop method from the list of cards

class Deck:
    
    def __init__(self):
        #User input is not required, so no need for self.smt=smt
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        #We have a Deck class,upon creating a new deck it creates an empty list which
        #then fills up with all the required cards;for suit in suits it creates a 
        #Card instantiation for each suit with all the different ranks(clubs->Two of Clubs, Three etc)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        #Note that random.shuffle doesn't return anything, it does the shuffling in place, 
        #meaning that it can't be assigned; I just want to know that the deck is shuffled
    
         
    def deal_one(self):
        return self.all_cards.pop()
                
        















# Deck class:

# Player class:

# Game Logic