from random import shuffle
from cards import Card
from wallet import Wallet

def shuffle_cards():
    '''
    Initial shuffle
    '''
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'JACK', 'QUEEN', 'KING']

    deck = []
    for suit in suits:
        for rank in ranks:
            card = Card(suit, rank)
            deck.append(card)
    shuffle(deck)

    return deck

def give_cards(deck):
    '''
    Give the first cards to the machine and player
    '''
    machine_hand = []
    player_hand = []

    machine_hand.append(deck.pop())
    machine_hand.append(deck.pop())

    player_hand.append(deck.pop())
    player_hand.append(deck.pop())

    return machine_hand, player_hand

def show_hands(machine_hand, player_hand):
    '''
    Show all the cards in the player and machines' hand
    '''
    print('==== Machine Hand ====')
    for card in machine_hand:
        print(card)

    print('\n==== Player Hand ====')
    for card in player_hand:
        print(card)

def bet():
    make_bet = Wallet(200)
    make_bet.get_balance()

deck = shuffle_cards()
machine_hand, player_hand = give_cards(deck)
show_hands(machine_hand, player_hand)

bet()