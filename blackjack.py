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

class Hand():
    def __init__(self):
        self.cards = [] # start with an empty list as we did in the Deck class
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribute to keep track of aces

    def add_card(self,card):
        # The card object that is passed in, is from the Deck class and specifically 
        # from Deck.deal() -> which yields a single Card(suit,rank) object
        self.cards.append(card) # We're then appending the card object in the self.cards empty list
        self.value += values[card.rank] # Then we're adjusting the total value of the hand (self.value)
                                        # with the value of the card that was added to the list - and 
                                        # we know that if self.value>21 -> lose
        # track aces
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        
        # First we check if self.value>21 check because we won't adjust an ace=1 if the self.value<21
        # (by default from the global dictionary, we consider an Ace of value = 11 )
        # Then, we also check if we *do* have an ace. If both checks are passed 
        # then we subtract 10 (which) is the adjustment for the ace, 
        # *AND* remove a count from self.aces (in order to break out of the while loop)
        while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self):
        self.total = 100 # Here this is a default value but we can opt in to have it passed
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# Functions #

# Function for taking bets:
def take_bet(chips:Chips): # We are taking some chips objects from the Chips class (that has a .total and .bet attribute)
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? ")) # We set the bet to what the player wants
        except:
            print("Sorry, please provide an integer!") # We check if the player is providing an integer
        else:
            if chips.bet > chips.total: # Even if they are providing an int, we check if they have enough chips
                print("Sorry, you don't have enough chips! You have: {} ".format(chips.total))
            else:
                break

# Function for taking hits:
def hit(deck:Deck,hand:Hand): # Takes the deck instance of Deck (however many cards left in it) and someone's 
                              # instance of Hand,
    single_card = deck.deal() # grabs a single card from the deck instance,
    hand.add_card(single_card)# adds it to the hand instance,
    hand.adjust_for_ace()     # and then checks for an ace adjustment

# Function prompting the player to Hit or Stand:
def hit_or_stand(deck:Deck,hand:Hand):
    # Takes in the deck instance and hand instance as arguments and assigns playing as a GLOBAL variable;
    # if the player hits, then we employ the hit() function, if the player stands then we set
    # the global playing variable to False which will act as a flag.
    global playing # This is for controlling the while loop later on (not the one below)

    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("Player stands! Dealer's turn")
            playing = False

        else:
            print("Sorry, I didn't understand that. Please enter 'h' or 's' only")
            continue
        break

# Functions to display cards:
def show_some(player:Hand,dealer:Hand): 
    # We want to show only ONE of the dealer's cards from their hand
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1]) # Shows only the card at index 1, ommitting the card at index 0

    # We want to show ALL (2 cards at the start of the game) from the player's hand
    # so we will go with a for loop for the entirety of the list .cards for the player instance 
    print("\n Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player:Hand,dealer:Hand):
    # Show all the dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    #**ALTERNATIVE WAY: #print("\n Dealer's hand: ",*dealer.cards,sep='\n')  --- avoids the for loop
    # Calculate and display the dealer's cards' value (since it happens at the end)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # Show all the player's cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    # Calculate and display the player's cards' value
    print(f"Value of Player's hand is: {player.value}")

# Write functions to handle end of game scenarios:
def player_busts(player:Hand,dealer:Hand,chips:Chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player:Hand,dealer:Hand,chips:Chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player:Hand,dealer:Hand,chips:Chips):
    print("BUST DEALER! PLAYER WINS!")
    chips.win_bet() # Note that when dealer busts player wins, so the player wins chips!

def dealer_wins(player:Hand,dealer:Hand,chips:Chips):
    print("DEALER WINS! PLAYER LOSES!")
    chips.lose_bet()# Note that when dealer wins player loses, so the player loses chips!


def push(player:Hand,dealer:Hand): # When both player and dealer get 21
    print("Dealer and player tie! PUSH!")



