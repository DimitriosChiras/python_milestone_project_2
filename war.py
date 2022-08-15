## 1) Have a deck, 2) shuffle it, 3) split it in two equal halves, 4) both players
## reveal simultaneously their top card and compare it, 4i) the card that has the
## higher ranking wins and the player that wins the matchup takes both cards and 
## puts them in their deck, 4ii) if the cards have the exact same value then it's WAR
## 5) WAR: both players take 3 cards face down and a last one face up: 5i) same as before
## the card with the higher ranking wins, 5ii) in case of another WAR, repeat,
## 5iii) if a player runs out of cards during war, then they lose.
## 6) WIN CONDITION: one player has gathered all of the cards

# Card class: it should:
# 1) Understand the suit of the card (hearts, diamonds clubs), 2) rank (1,2,3....king)
# and 3) an easy-to-use integer value corresponding to that rank so that we can compare 
# later on 2 instances of the card class and decide which card has the higher value

class Card:
# When someone creates an instance of the card they should provide the suit 
# and rank of the card (the value we don't need as it will be calcullated from a dictionary)
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank  
    def __str__(self):
        return self.rank + " of " + self.suit #Assumes that rank and suit passed in are strings

two_hearts = Card("hearts","Two")

print(two_hearts)











# Deck class:

# Player class:

# Game Logic