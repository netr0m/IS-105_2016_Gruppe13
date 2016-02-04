## -*- coding: utf-8 -*-
# Pokerspill for gruppe 13, IS-105
# Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
import collections
import itertools
import random

SUIT_VALUES = ("Hearts", "Spades", "Diamonds", "Clubs")
CARD_VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

class card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.card = self.value, self.suit
    def __repr__(self):
        return self.value + "-" + self.suit
    
class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Nothing"
        value_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            value_dict[my_card.value] += 1
            suit_dict[my_card.suit] += 1
        # Pair
        if len(value_dict) == 4:
            short_desc = "One pair"
        # Two pairs or 3-of-a-kind
        elif len(value_dict) == 3:
            if 3 in value_dict.values():
                short_desc = "Three-of-a-kind"
            else:
                short_desc = "Two pairs"
        # Full house or 4-of-a-kind
        elif len(value_dict) == 2:
            if 2 in value_dict.values():
                short_desc = "Full House"
            else:
                short_desc = "Four of a kind"
        else:
            #Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_value = min([CARD_VALUES.index(x) for x in value_dict.keys()])
            max_value = max([CARD_VALUES.index(x) for x in value_dict.keys()])
            if int(max_value) - int(min_value) == 4:
                straight = True
            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(value_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc = "Straight"
            elif flush and not straight:
                short_desc = "Flush"
            elif flush and straight:
                short_desc = "Straight flush"
            enumeration = "/".join([str(x) for x in self.card_list])
            return "{enumeration} ({short_desc})".format(**locals())
        
class deck(set):
    def __init__(self):
        for value, suit in itertools.product(CARD_VALUES, SUIT_VALUES):
            self.add(card(value, suit))
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return poker_hand([self.get_card() for x in range (number_of_cards)])
        else:
            raise NotImplementedError
        
for i in range(100000):
    print(deck().get_hand())