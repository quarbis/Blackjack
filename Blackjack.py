import random


card_values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "jack", "king", "queen"]
suits = ["hearts", "spades", "clubs", "diamonds"]
cards = [(card, suit) for card in card_values for suit in suits]

def deal_card(list):
    card, suit = random.choice(cards)
    list.append([card, suit])
    return card, suit

def card_list(player_cards):
    card_list = ""
    for i in range(len(player_cards)):
        card_list += "a {} of {}".format(player_cards[i][0], player_cards[i][1])
        if i <= len(player_cards) - 2 and len(player_cards) > 2:
            card_list += ","
        card_list += " "
        if i == len(player_cards) - 2:
            card_list += "and "
    return card_list

def print_player_cards(player_cards):
    player_hand = "You have " + card_list(player_cards)
    print("\n" + player_hand)
    


def print_dealers_card(dealer_cards):
    card_value, suit = dealer_cards[1]
    string = "The dealer has a {} of {}".format(card_value, suit)
    print("\n" + string)
    
    

def choices(dealer_cards, player_cards):
    choices = {"S": "stand", "H": "hit"}
    if len(player_cards) == 2:
        choices["D"] = "double"
    if dealer_cards[1][0] == "ace":
        choices["I"] = "insurance"
    return choices
    
def print_choices(dealer_cards, player_cards):
    print("\nPress: ")
    choice_list = choices(dealer_cards, player_cards)
    for letter, move in choice_list.items():
        print("{} for {}".format(letter, move))
    print()

def find_value(cards):
    total = 0
    aces = 0
    for card_face, suit in cards:
        if card_face.is_digit():
            total += int(card_face)
            continue
        if card_face in ["king", "queen", "jack"]: 
            total += 10
        if card_face == "ace":
            aces += 1
    for i in range(aces):
        if total + 11 <= 21:
            total += 11
        else: 
            total += 1
    return total

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

        
        match player_move:
            case "H":
                card, suit = deal_card(player_cards)
                print("\nYou got a {} of {}".format(card, suit))
            case "S":
                break
            case "D":
                bet *= 2
                print("\nYour bet is now ${}".format(bet))
            case "I":
                pass
        

print("------Blackjack------")
print("Insurance pays 2 to 1")
print("Blackjack pays 3 to 2\n")
round(20)