####################################################
####WElcome TO War Card Game OOP Pytohn Porject####
###################################################
# --------------Start ---------------------
from random import shuffle  # for random rounds
# --------Card Part --:--
SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
# --------Classes Part --:--


class Deck:
    """
    This is the Deck Class. THis object will create a deck of cards
    to initiate play. You can then use this Deck list of cards to
    split in half and give to the players. It will use SUITE and
    RANKS to create the deck. It should also have a method for
    spiltting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle_random(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_card_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    This is the Player class, which takes in a name and an instance
    of a Hand class object. The Player can then play cards and
    check if they still have cards
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".fromat(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the PLayer class,which takes in a name and instance
    of Jand class object. The Player can then play cards and
    check if they still have cards
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        push_card = self.hand.remove_card()
        print(f'{self.name} has place: {push_card}')
        print("\n")
        return push_card

    def remove_war_cards(self):

        war_cards = []
        if (len(self.hand.cards) < 3):
            return self.hand.cards
        else:

            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards lef
        """
        return len(self.hand.cards) != 0


# -------------part of gmae inst
#########################
#### Area of the Game####
##########################
print("Welcome to War Card Game, let's begin ...")

# 1- Create new deck and split it in half:

d = Deck()
d.shuffle_random()
half1, half2 = d.split_card_half()


# 2- Create both Players
player_PS = Player("Computer", Hand(half1))

name = input("What is your Name ? ")

player_user = Player(name, Hand(half2))

total_round = 0
war_count = 0

while player_user.still_has_cards() and player_PS.still_has_cards():
    total_round += 1
    print("Time for New round !")
    print("here are the current standing")
    print(player_user.name+" has the count:"+str(len(player_PS.hand.cards)))
    print(player_PS.name+" has the count:"+str(len(player_PS.hand.cards)))
    print("Play a card !")
    print('\n')

    table_card = []
    ps_card = player_PS.play_card()
    u_card = player_user.play_card()

    table_card.append(ps_card)
    table_card.append(u_card)

    if ps_card[1] == u_card[1]:
        war_count += 1

        print("War !")
        table_card.extend(player_user.remove_war_cards())
        table_card.extend(player_PS.remove_war_cards())
        if RANKS.index(ps_card[1]) < RANKS.index(u_card[1]):
            player_user.hand.add(table_card)
        else:
            player_PS.hand.add(table_card)

    else:
        if RANKS.index(ps_card[1]) < RANKS.index(u_card[1]):
            player_user.hand.add(table_card)
        else:
            player_PS.hand.add(table_card)
print("Game Over,numer of round:"+str(total_round))
print("A war happend "+str(war_count)+" times")
print("Does the computer still have cards ? ")
print(str(player_PS.still_has_cards()))
print("Does the "+player_user.name+" still have cards ? ")
print(str(player_user.still_has_cards()))