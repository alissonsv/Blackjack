from random import shuffle
from cards import Card

def bet(balance):
    '''
    Initial bet for the game
    '''
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

def hit(player, deck):
    '''
    Give cards to any player
    '''
    player.append(deck.pop())
    return player
    

def show_hands(machine_hand, player_hand, player_turn=True):
    '''
    Show all the cards in the player and machines' hand
    '''
    print('\n==== Machine Hand ====')
    if player_turn:
        print('[Face Down]')
        print(machine_hand[1])
    else:
        for card in machine_hand:
            print(card)
        print("\nDealer's total: " + str(sum_cards(machine_hand)))

    print('\n==== Player Hand ====')
    for card in player_hand:
        print(card)
    print("\nYour total: " + str(sum_cards(player_hand)))

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
    if sum_cards(hand) == 21:
        print("\nTWENTY ONE!!!")
        return True
    
    return False

def end_game(bet_amount, balance, winner='machine'):
    if winner == 'player':
        print("CONGRATULATIONS!\nYOU WON!")
        balance += bet_amount
    else:
        print("THE DEALER WON!")
        balance -= bet_amount

    return balance

def round(deck, bet_amount, balance, player_hand, machine_hand):
    # Player has 21
    if has_21(player_hand):
        balance = end_game(bet_amount, balance, winner='player')
    else:
        # Dealer has 21
        if has_21(machine_hand):
            balance = end_game(bet_amount, balance, winner='dealer')
        else:
            # Player want to STAY or HIT
            response = ''
            while response not in ['hit', 'h', 's', 'stay']:
                response = input("Do you want to HIT or STAY?\n(hit or h / stay or s): ").lower()
            
            # HIT
            if response in ['h', 'hit']:
                player_hand = hit(player_hand, deck)
                show_hands(machine_hand, player_hand)

                score = sum_cards(player_hand)
                if score > 21:
                    balance = end_game(bet_amount, balance, winner='dealer')
                else:
                    balance = round(deck, bet_amount, balance, player_hand, machine_hand)
            # STAY
            else:
                player_score = sum_cards(player_hand)
                machine_score = sum_cards(machine_hand)

                while True:
                    machine_hand = hit(machine_hand, deck)
                    show_hands(machine_hand, player_hand, player_turn=False)
                    machine_score = sum_cards(machine_hand)

                    if has_21(machine_hand):
                        balance = end_game(bet_amount, balance, winner='dealer')
                        break
                    elif machine_score > player_score and machine_score < 21:
                        balance = end_game(bet_amount, balance, winner='dealer')
                        break
                    elif machine_score > 21:
                        balance = end_game(bet_amount, balance, winner='player')
                        break
                    
    
    return balance

def replay(balance):
    machine_hand = []
    player_hand = []

    bet_amount = bet(balance)
    deck = shuffle_cards()
    
    #Give the first two cards to the player and machine
    for x in range(2):
        machine_hand = hit(machine_hand, deck)
        player_hand = hit(player_hand, deck)

    show_hands(machine_hand, player_hand)
    balance = round(deck, bet_amount, balance, player_hand, machine_hand)

    return balance

if __name__ == '__main__':    
    balance = 100
    print('WELCOME TO THE BLACKJACK GAME!!!')
    
    play_again = 'Y'
    while play_again == 'Y':
        if balance == 0:
            print("Your balance reached to 0!\nYou're broke! :(")
        print(f"Here's your actual balance: {balance}" )
        balance = replay(balance)
        play_again = input('Do you want to play again? (Y/N) ').upper()