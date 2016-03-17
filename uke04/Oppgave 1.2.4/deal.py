# -*- coding: utf-8 -*-
# Group 13, upcoming Poker program
# Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
import random # Imports the random module.

# Deal function, deals n number of cards to each player from the list "deck".
def deal(numhands, n=5, deck=[ranks+suits for ranks in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] for suits in [' of Spades', ' of Hearts', ' of Diamonds', ' of Clubs']]):
    random.shuffle(deck) # Shuffles the deck by using the random module, and then deals the cards.
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

print "The dealer dealt these cards:\n"
print deal(5)    # Use the parameter here to define how many players the dealer should deal to