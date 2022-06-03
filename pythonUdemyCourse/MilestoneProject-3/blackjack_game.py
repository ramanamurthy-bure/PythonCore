# blackjack game
# Game Play
# 1. create a deck of 52 cards
# 2. shuffle the deck
# 3. ask the player for their bet
# 4. make sure the players bet does not exceed their available chips
# 5. deal two cards to the dealer and two cards to the player
# 6. show only one of the dealer's cards, the other remains hidden
# 7. show both of the player's card
# 8. ask the player if they wish to hit. and take another card
# 9. if the players hand doesn't bust (go over 21), ask if they would like to Hit again
# 10. If a player stands,play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11. Determine the winner and adjust the players chips accordingly
# 12. Ask the player if they would like to play again

'''
Playing Cards:
A standard deck of playing cards has four suits(Hearts,Diamonds,Spades and Clubs) and thirteen
ranks (2 throught 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck.
Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without
busting. As a starting point in your program, you may want to assign variables to store a list of suits, ranks,
and then use a dictionary to map ranks to values.

The Game:
Step-1: import the random module. This will be used to shuffle the deck prior to dealing. Then declare variable to store
suits, ranks and values. You can develop your own system, or copy ours below. Finally,declare a Boolean
value to be used to control while loops. This is aa common practice used to control the flow of the game

Class Definition:
Consider making a card class where each Card object has a suit and a rank, then a Deck class to hold all 52 Card
Objects, and can be shuffled, and finally a Hand class holds those Cards that have been dealt to each player
from the Deck.

Step-2: Create a Card Class:
A Card object really only needs two attributes: suite and rank. You might add an attribute for 'value'.We chose
to handle value later when developing our Hand class.

In addition to the Card's __init__ mehtod, consider adding a __sts__ method that when asked to print a Card,
returns a string in the form 'Two of Hearts'

Step-3: Create a Deck Class:
Here we might store 52 card objects in a list that can later be shuffled. First, though, we need to instantiate
all 52 unique card objects and add them to our list . So long as the Card class definition appears in our code,
We can build Card objects inside our Deck __init__ method.Considering iterating over the sequences of suits and ranks
to build out each card. This might appear inside a Deck class __init__ method.
        for suite in suits:
            for rank in ranks:
In addition to an __init__ method we will also want to add methods to shuffle our deck, and to deal out
cards during game play
Optional : We may never need to print the contents of the deck during the gameplay, but having the ability to
see the cards inside it may help troubleshoot any problem that occur during the game development.
With this in mind consider adding __str__ method to the class definition

Step-4: Create a Hand Class:
In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those
cards using the values dictionary defined above. It may also need to adjust for the value of Aces when appropriate

Step-5: Create a Chip Class:
In addition to decks of cards and hands, we need to keep track of a Player's starting chips,bets, and ongoing
winnings. This could be done using global variables, but in the spirit of objects oriented programming. Let's
make a Chip class instead!

Function Definitions:
A lot of steps are going to be repretitive. That's where functions come in!. The following steps are guidelines
add or remove functions as needed in your own program.

Step-6: Write a function for taking bets
Since we are asking the user for an integer value. This would be a good place to use try/except. Remember to check
that a Player's bet can be covered by their available chips.

Step-7: Write a function for taking hits
Either player can take hits until they bust. This function will be called during gameplay anytime a player
requests a hit or a Dealer's hand is less than 17. It should take inn Deck and Hand objects as arguments, and
deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a Player's
hand exceeds 21.

Step-8 : Write a function prompting the player to Hit or stand
This function should accept the deck and player's hand as arguments, and assign playing as a global variable.
If the Player Hits, employ the hit() function above . If the Player Stands, set the playing variable to False -
this will control the behaviour of a while loop later on in our code

Step-9 : Write a function to display cards
When the game starts, and after each time Player takes card, the dealer's first card is hidden and all of Players
cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value.
Write a function for each of these scenarios.

Step-10 : Write a function to handle end of game scenario
Remember to pass player's hand, dealer's hand and chips as needed

'''

import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return self.rank+" of "+self.suite

class Deck():
    def __init__(self):
        self.deck = [] # start with an empty list
        for suite in suits:
            for rank in ranks:
                self.deck.append(Card(suite,rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return "The deck has: "+deck_comp


    def shuffe(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = [] # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0 # add an attribute to keep track of aces

    def add_card(self,card):
        # card passed in
        # from Deck.deal() --> Single Card(suite,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # Track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21 and I still have an ace
        # Then change my ace to be a insted of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100 # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer ")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! you have: {} '.format(chips.total))
            else:
                break
                
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print('Sorry, I did no understand that, Please enter h or s only! ')
            continue
        break
        
def show_some(player,dealer):
    # show only ONE of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden! ")
    print(dealer.cards[1])
    # show all(2 cards) of the player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # show all the dealer's cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print("\n Dealer's hand: ",dealer.cards,sep='\n')
    # calculate and display value(j+k == 20)
    print(f"value of Dealer's hand is: {dealer.value}")
    # show all the players cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! Push!")

