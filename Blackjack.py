import random


card_values = list(range(2, 11)) + ["jack", "king", "queen", "ace"]
suits = ["hearts", "spades", "clubs", "diamonds"]

cards = [(card, suit) for card in card_values for suit in suits]

def deal_card(list):
    card, suit = random.choice(cards)
    list.append([card, suit])

def card_list(player_cards):
    card_list = ""
    for i in range(len(player_cards)):
        card_list += "a " + str(player_cards[i][0]) + " of " + player_cards[i][1]
        if i >= len(player_cards) - 2 and len(player_cards) > 2:
            card_list += ","
        card_list += " "
        if i == len(player_cards) - 2:
            card_list += "and "
    return card_list

def print_player_cards(player_cards):
    player_hand = "You have " + card_list(player_cards)
    print()
    print(player_hand)
    


def print_dealers_card(dealer_cards):
    card_value, suit = dealer_cards[1]
    string = "The dealer has a " + str(card_value) + " of " + suit
    print()
    print(string)
    
    

def choices(dealer_cards, player_cards):
    choices = {"S": "stand", "H": "hit"}
    if len(player_cards) == 2:
        choices["D"] = "double"
    if dealer_cards[1][0] == "ace":
        choices["I"] = "insurance"
    return choices
    
def print_choices(dealer_cards, player_cards):
    print()
    print("Press: ")
    choice_list = choices(dealer_cards, player_cards)
    for letter, move in choice_list.items():
        print(letter + " for " + move)
    print()

def round(bank):
    print("You have ${}".format(bank))
    
    while True:
        bet = input("How much do you want to bet?\n")
        if bet.isdigit() and 1 <= int(bet) <= bank:
            break
        else:
            print("Invalid amount")

    print("You bet {} dollars".format(bet))

    player_cards = []
    
    dealer_cards = []

    for i in range(2):
        deal_card(player_cards)
        deal_card(dealer_cards)

    while True:

        print_dealers_card(dealer_cards)

        print_player_cards(player_cards)

        print_choices(dealer_cards, player_cards)

        while True:
            player_move = input()
            if player_move in choices(dealer_cards, player_cards).keys():
                break
            else:
                print("invalid input, try again:")
        
            

round(20)