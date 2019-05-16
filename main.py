from random import shuffle
from cards import Card

def bet(balance):
    while True:
        try:
            bet_amount = int(input('How much do you want to bet? '))
            if bet_amount > 0 and bet_amount <= balance:
                print('Bet done!')
                break
            else:
                print('The bet need to be greater than 0 and less or equal your balance!\n')
                continue
        except ValueError:
            print('Please, type a number to bet!\n')
        
    return bet_amount

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
    

def show_hands(machine_hand, player_hand, player_turn=True):
    '''
    Show all the cards in the player and machines' hand
    '''
    print('==== Machine Hand ====')
    if player_turn:
        print('[Face Down]')
        print(machine_hand[1])
    else:
        for card in machine_hand:
            print(card)

    print('\n==== Player Hand ====')
    for card in player_hand:
        print(card)

#deck = shuffle_cards()
#machine_hand, player_hand = give_cards(deck)
#show_hands(machine_hand, player_hand)


if __name__ == '__main__':
    balance = 100
    bet_amount = bet(balance)