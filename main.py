'''
author: Alisson Vargas

A Blackjack Game
'''
import os
import time
from random import shuffle
from cards import Card

def clear_screen():
    '''
    Clear the screen based on OS
    '''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def bet():
    '''
    Initial bet for the game
    '''
    while True:
        try:
            bet_amount = int(input('How much do you want to bet? '))
            if 0 < bet_amount <= BALANCE:
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

def hit(player, deck):
    '''
    Give cards to any player
    '''
    player.append(deck.pop())
    return player

def show_hands(dealer_hand, player_hand, player_turn=True):
    '''
    Show all the cards in the player and dealers' hand
    '''
    clear_screen()
    print('\n==== Dealer Hand ====')
    if player_turn:
        print('[Face Down]')
        print(dealer_hand[1])
    else:
        for card in dealer_hand:
            print(card)
        print("\nDealer's total: " + str(sum_cards(dealer_hand)))

    print('\n==== Player Hand ====')
    for card in player_hand:
        print(card)
    print("\nYour total: " + str(sum_cards(player_hand)) + "\n\n\n\n")

def sum_cards(hand):
    '''
    Sum the cards values in the hand
    '''
    total = 0
    for card in hand:
        total += card.value

    #changes the value of the first Ace to '1' if the player is busted
    #and if he's still busted rerun sum_cards
    aces = [card for card in hand if card.value == 11]
    if total > 21 and aces != []:
        aces[0].value = 1
        total = sum_cards(hand)

    return total

def has_21(hand):
    '''
    Tests if the player has 21 and return a boolean
    '''
    if sum_cards(hand) == 21:
        print("\nTWENTY ONE!!!")
        return True

    return False

def end_game(bet_amount, winner='dealer'):
    '''
    Congratulates the winner and return the balance
    '''
    global BALANCE
    if winner == 'player':
        print("CONGRATULATIONS!\nYOU WON!")
        BALANCE += bet_amount
    else:
        print("THE DEALER WON!")
        BALANCE -= bet_amount

def round(deck, bet_amount, player_hand, dealer_hand):
    '''
    Do all the round play and return balance
    '''
    # Player has 21 - Double the bet
    if has_21(player_hand):
        end_game(bet_amount*2, winner='player')
    else:
        # Dealer has 21
        if has_21(dealer_hand):
            end_game(bet_amount, winner='dealer')
        else:
            # Player want to STAY or HIT
            response = ''
            while response not in ['hit', 'h', 's', 'stay']:
                response = input("Do you want to HIT or STAY?\n(HIT or H / STAY or S): ").lower()

            # HIT
            if response in ['h', 'hit']:
                player_hand = hit(player_hand, deck)

                score = sum_cards(player_hand)
                if score > 21:
                    show_hands(dealer_hand, player_hand, player_turn='False')
                    end_game(bet_amount, winner='dealer')
                else:
                    show_hands(dealer_hand, player_hand)
                    round(deck, bet_amount, player_hand, dealer_hand)
            # STAY
            else:
                player_score = sum_cards(player_hand)
                dealer_score = sum_cards(dealer_hand)
                print(f"PLAYER_SCORE = {player_score}\nMACHINE_SCORE = {dealer_score}")
                while True:
                    show_hands(dealer_hand, player_hand, player_turn=False)
                    dealer_score = sum_cards(dealer_hand)

                    if has_21(dealer_hand):
                        end_game(bet_amount, winner='dealer')
                        break
                    elif player_score < dealer_score < 21:
                        end_game(bet_amount, winner='dealer')
                        break
                    elif dealer_score > 21:
                        end_game(bet_amount, winner='player')
                        break

                    time.sleep(1)
                    dealer_hand = hit(dealer_hand, deck)

def replay():
    '''
    replay the initial functions
    '''
    dealer_hand = []
    player_hand = []

    bet_amount = bet()

    print('shuffling the cards...')
    time.sleep(1)
    clear_screen()

    deck = shuffle_cards()

    #Give the first two cards to the player and dealer
    for _ in range(2):
        dealer_hand = hit(dealer_hand, deck)
        player_hand = hit(player_hand, deck)

    show_hands(dealer_hand, player_hand)
    round(deck, bet_amount, player_hand, dealer_hand)

if __name__ == '__main__': 
    BALANCE = 100

    clear_screen()
    print("=======================================")
    print('==   WELCOME TO THE BLACKJACK GAME   ==')
    print("=======================================\n")

    PLAY_AGAIN = 'Y'
    while PLAY_AGAIN in ('Y', ''):
        print(f"Here's your actual balance: {BALANCE}")

        replay()
        if BALANCE == 0:
            print("Your balance reached to 0!\nYou're broke! :(")
            break
        PLAY_AGAIN = input('\nDo you want to play again? (Y/n) ').upper()
        clear_screen()