# Card
import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suite


class Deck():
    def __init__(self):
        self.allcards = []
        for suite in suits:
            for rank in ranks:
                # Create the card object
                createdcard = Card(suite,rank)
                self.allcards.append(createdcard)

    def shuffle(self):
        random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()


class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards. '


# Game Setup
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(len(player_one.all_cards))
# While game_on
round_num = 0
game_on = True

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards!, Player Two wins')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards!, Player One wins')
        game_on = False
        break

    #start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at war
    # Now its time to check the players cards against each other
    # There are lots of ways this can be done!
    # We have 3 situations:
    # 1. Player One > Player Two
    # 2. Player One < Player Two
    # 3. Player One == Player Two
    # The way we will write this is with an if/elif/else within a while loop that assumes that a 'war' has happened
    # We will state at_war=False if the players resolve the match-up on the first drawn card, otherwise we will
    # add cards to the current cards on the table
    # The rules we will use in this version is if there is a tie, each player needs to draw 5 additional cards
    # We will also say that a player loses if they don't have at least 5 cards to play the war
    # This logic is easily edited to fit any rule structure you want

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare the war")
                print("Player Two Wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare the war")
                print("Player One Wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())







