'''
Poker hands
Problem 54


In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have a
pair of queens, then highest cards in each hand are compared (see example 4 below);
 if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:


The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
 each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

'''
import collections

def winner(hand1, hand2):

    hand1val = -1
    hand2val = -1

    if is_royal_flush(hand1):
        hand1val = 0
    elif is_straight_flush(hand1):
        hand1val = 1
    elif is_four_of_a_kind(hand1):
        hand1val = 2
    elif is_full_house(hand1):
        hand1val = 3
    elif is_flush(hand1):
        hand1val = 4
    elif is_straight(hand1):
        hand1val = 5
    elif is_three_of_a_kind(hand1):
        hand1val = 6
    elif is_two_pairs(hand1):
        hand1val = 7
    elif is_one_pairs(hand1):
        hand1val = 8
    else:
        hand1val = 9


    if is_royal_flush(hand2):
        hand2val = 0
    elif is_straight_flush(hand2):
        hand2val = 1
    elif is_four_of_a_kind(hand2):
        hand2val = 2
    elif is_full_house(hand2):
        hand2val = 3
    elif is_flush(hand2):
        hand2val = 4
    elif is_straight(hand2):
        hand2val = 5
    elif is_three_of_a_kind(hand2):
        hand2val = 6
    elif is_two_pairs(hand2):
        hand2val = 7
    elif is_one_pairs(hand2):
        hand2val = 8
    else:
        hand2val = 9


    if hand1val == 9 and hand2val == 9:
        if high_card(hand1) > high_card(hand2):
            return 1
        if high_card(hand2) > high_card(hand1):
            return 2



    if hand1val < hand2val:
        return 1
    elif hand1val > hand2val:
        return 2
    else:
        print(hand1val)
        return 0




def is_royal_flush(hand):
    if same_suite(hand):
            hand.sort()
            #print(hand)
            if hand[0][0] == 'A' and hand[1][0] == 'J' and hand[2][0] == 'K' and hand[3][0] == 'Q' and hand[4][0] == 'T':
                return True
    return False

def is_straight_flush(hand):
    if same_suite(hand):
        vals = list_valeus(hand)
        if vals[0] == vals[1] - 1 and vals[1] == vals[2] - 1 and vals[2] == vals[3] - 1 and vals[3] == vals[4] - 1:
            return True
    return False

def is_four_of_a_kind(hand):
    vals  = list_valeus(hand)
    counter=collections.Counter(vals)

    if 4 in counter.values():
        return True
    return False

def is_flush(hand):
    if same_suite(hand):
        return True
    return False

def is_straight(hand):
    vals = list_valeus(hand)
    if vals[0] == vals[1] - 1 and vals[1] == vals[2] - 1 and vals[2] == vals[3] - 1 and vals[3] == vals[4] - 1:
        return True
    return False

def is_three_of_a_kind(hand):
    vals  = list_valeus(hand)
    counter=collections.Counter(vals)

    if 3 in counter.values():
        return True
    return False

def is_full_house(hand):
    vals  = list_valeus(hand)
    counter=collections.Counter(vals)

    if 3 in counter.values() and 2 in counter.values()  :
        return True
    return False

def is_two_pairs(hand):
    vals  = list_valeus(hand)
    counter=collections.Counter(vals)

    vals = counter.values()

    count = 0
    for i in range(0, len(vals)):
        if vals[i] > 1:
            count += 1

    if count > 1:
        return True

    return False

def is_one_pairs(hand):
    vals = list_valeus(hand)
    counter=collections.Counter(vals)

    vals = counter.values()

    count = 0
    for i in range(0, len(vals)):
        if vals[i] > 1:
            count += 1

    if count > 0 :
        return True

    return False

def high_card(hand):
    vals = list_valeus(hand)
    return vals[4]


def same_suite(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    return False

def list_valeus(hand):
    hand = [dict[hand[0][0]],dict[hand[1][0]],dict[hand[2][0]],dict[hand[3][0]],dict[hand[4][0]]]
    hand.sort()
    return hand



dict = {'2' : 0,'3': 1,'4' : 2, '5' : 3 , '6' : 4, '7' : 5 , '8' : 6 ,'9' : 7,'T' : 8,'J' : 9, 'Q' : 10,'K' : 11 , 'A' : 12 }

with open('poker.txt') as f:
    hands = f.read().splitlines()


hands = [line.split() for line in hands]


#print(hands)

#print(hands[0][0][0])

print( winner(['7C', '7C', '8C', '4C', '5D'],['7D', '7C', '7C', '4C', '5C']))

p1wins = 0
p2wins = 0
ties = 0

for lines in hands:
    win = winner(lines[0:5],lines[5:10])

    if win == 1:
        p1wins += 1

    if win == 2:
        p2wins += 1

    if win == 0:
        ties += 1


print(p1wins)
print(p2wins)
print(ties)
