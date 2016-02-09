# -*- coding: utf-8 -*-
# Card dealer for upcoming Poker program
# Group 13
# Members: Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen

# Import sentence to import the random and itertools modules
import random
import itertools

# Define card values and suits
SUITS = [' of Hearts', ' of Spades', ' of Diamonds', ' of Clubs']
CARD_VALUES = ['2 ', '3', '4', '5','6', '7', '8', '9','10', 'Jack', 'Queen', 'King', 'Ace']

# Randomize cards for each hand
DECK = tuple(''.join(card) for card in itertools.product(CARD_VALUES, SUITS))
hand = random.sample(DECK, 5)

# Print the hand of the first player
print "First player\'s hand:"
print hand
print "\n"

# Print the hand of the second player
hand = random.sample(DECK, 5)

print "Second player\'s hand:"
print hand
print "\n"

# Print the hand of the third player
hand = random.sample(DECK, 5)

print "Third player\'s hand:"
print hand
print "\n"

# Print the hand of the fourth player
hand = random.sample(DECK, 5)

print "Fourth player\'s hand:"
print hand
print "\n"

# Print the hand of the fifth player
hand = random.sample(DECK, 5)

print "Fifth player\'s hand:"
print hand
print "\n"