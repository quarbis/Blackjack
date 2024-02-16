import random


card_values = list(range(2, 11)) + ["jack", "king", "queen", "ace"]
suits = ["hearts", "spades", "clubs", "diamonds"]

cards = [(card, suit) for card in card_values for suit in suits]

def deal_card():
    card, suit = random.choice(cards)
    return [card, suit]
    
def display_cards(dealer_cards, player_cards):
    print()
    player_hand = "You have "
    for i in range(len(player_cards)):
        player_hand += "a " + str(player_cards[i][0]) + " of " + player_cards[i][1]
        if i >= len(player_cards) - 2 and len(player_cards) > 2:
            player_hand += ","
        player_hand += " "
        if i == len(player_cards) - 2:
            player_hand += "and "
    dealer_hand = "The dealer has "
    for i in range(len(dealer_cards)):
        dealer_hand += "a " + str(player_cards[i][0]) + " of " + player_cards[i][1]
        if i < len(dealer_cards) - 1 and len(dealer_cards) > 2:
            dealer_hand += ","
        dealer_hand += " "
        if i == len(dealer_cards) - 2:
            dealer_hand += "and "
    print(player_hand)
    print(dealer_hand)
    

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

    player_cards = [deal_card(), deal_card()]
    
    dealer_cards = [deal_card(), deal_card()]

    display_cards(dealer_cards, player_cards)

    print_choices(dealer_cards, player_cards)

    while True:
        player_move = input()
        if player_move in choices(dealer_cards, player_cards).keys():
            break
        else:
            print("invalid input, try again:")
        

