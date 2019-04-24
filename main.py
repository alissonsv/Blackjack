from random import shuffle
from cards import Card

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'JACK', 'QUEEN', 'KING']

deck = []

for suit in suits:
    for rank in ranks:
        card = Card(suit, rank)
        deck.append(card)

shuffle(deck)

for card in deck:
    print(card)