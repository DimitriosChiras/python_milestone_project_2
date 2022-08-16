## 1) Have a deck, 2) shuffle it, 3) split it in two equal halves, 4) both players
## reveal simultaneously their top card and compare it, 4i) the card that has the
## higher ranking wins and the player that wins the matchup takes both cards and 
## puts them in their deck, 4ii) if the cards have the exact same value then it's WAR
## 5) WAR: both players take 3 cards face down and a last one face up: 5i) same as before
## the card with the higher ranking wins, 5ii) in case of another WAR, repeat,
## 5iii) if a player runs out of cards during war, then they lose.
## 6) WIN CONDITION: one player has gathered all of the cards

"------------------------------------------------------------------------------------------"
#GAME LOGIC
#First we create 2 instances of the Player class: Player 1&2. 
#Then we create an instance of a new deck which we will shuffle and then split it between 
#player 1&2. Players have now half the deck. Now, in order to go through the game logic, we should 
#check if someone has already lost- ie check for zero cards - ie if the len of the all_cards list 
#is equal to zero. At the beginning we know that's not the case but we go through this check
#in order to begin (and in each consecutive round). If the len is not zero, then we can have 
#a boolean value (game_on) act as a flag if equal to True to continue the game. Then we have a while game_on during which each player pops a card which we compare.
#Depending on who won the comparison, the winner can either append the card which goes to the
#bottom of their hand (all_cards), or continue to WAR. In this case, players draw 
#additional 3 cards - so we will have a while at_war loop, with at_war being the flag for WAR.
#Whoever wins the WAR(s) gets their all_cards list .extend() with the flipped cards.
#Then we run the empty all_cards check again and if it comes true, we have a winner!

"-------------------------------------------------------------------------------------------"
#CLASSES:

# Card class: 
# It should 1) Understand the suit of the card (hearts, diamonds clubs), 2) rank (1,2,3....king)
# and 3) an easy-to-use integer value corresponding to that rank so that we can compare 
# later on 2 instances of the card class and decide which card has the higher value

# Deck class:
# It should 1) instantiate a new deck (create all 52 card objects AND hold them as a LIST of card objects)
# 2) shuffle a deck through the shuffle() function from the random library and 3) deal cards from
# the Deck object using the Pop method from the list of cards

# Player class:
# We need to translate a Deck/Hand of cards with a top and bottom, to a Python list
# .pop(0) removes the top (beginning of the list) card, .append() works for SINGLE cards being
# added to the end of the list - we will use .extend() as this allows to add MULTIPLE cards
# at the end of a list without creating nested lists

"-------------------------------------------------------------------------------------------"


import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
# When someone creates an instance of the card they should provide the suit 
# and rank of the card (the value we don't need as it will be calcullated from a dictionary)
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit #Assumes that rank and suit passed in are strings

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
                
class Player:
    
    def __init__(self,name):
        
        self.name=name    #Player should have a name
        self.all_cards=[] #Player should have an empty hand
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards): #new_cards can be a single Card object or a list of card objects
        if type(new_cards) == type([]):#to check this, I check if the type of the new_cards variable is the same with the one of an empty list
            #In this case we are adding a list of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            #In this case we are adding a single new Card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
        

# Game setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

#Splitting the deck in half between the 2 players (26 each):
for x in range (26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# Game logic

round_num = 0 #Counter for rounds

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards)==0:
        print("Player 1 out of cards! Player 2 wins!")
        game_on = False
        break
        
    if len(player_two.all_cards)==0:
        print("Player 2 out of cards! Player 1 wins!")
        game_on = False
        break
    
    #Start a new round
    player_one_cards = [] #Variable of the cards that a player leaves on the table -- NOT the same as player_one.all_cards
    player_one_cards.append(player_one.remove_one())
    #To start a new round, we remove a card from the .all_cards list of each player and append it to the cards currently in play (player_one_cards)
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    #Note that we .append-so the "top" card on the table is actually the LAST one 
    #in the player_one/two_cards lists , ie [-1]
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            #See above for [-1], and also player_one/two_cards is eventually going
            #to be a list of card class instances
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            
        else:
            print("WAR!!!")
            
            if len(player_one.all_cards) < 5: #Check if players' hands have enough cards
                print("Player 1 unable to declare war")
                print("Player 2 wins")
                game_on = False
                break #Breaks out of the while at_war loop and then the game_on=False leads to the break of the overall one
            
            elif len(player_two.all_cards) < 5:
                print("Player 2 unable to declare war")
                print("Player 1 wins")
                game_on = False
                break 
            
            else: #Draw 3 additional cards for each player
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    #Each player's table gets added a .remove_one card from player's hand, 3 times
    
    