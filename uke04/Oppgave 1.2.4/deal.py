# -*- coding: utf-8 -*-
# Group 13
# Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen

# Imports the random module.
import random

# Deal function, deals n number of cards to each player from the list "deck".
# Ranks (2, Jack, Queen etc.) and Suits (Hearts, Diamonds etc.)
def deal(numhands, n=5, deck=[ranks+suits for ranks in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] for suits in [' of Spades', ' of Hearts', ' of Diamonds', ' of Clubs']]):
    # Shuffles the deck by using the random module, and then deals the cards.
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

# Use the parameter here to define how many players the dealer should deal to
# Up to (10) players allowed, since we only use one deck of cards
print "The dealer dealt these cards:\n"
print deal(5)  
