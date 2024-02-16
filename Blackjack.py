import random


card_values = list(range(2, 11)) + ["jack", "king", "queen", "ace"]
suits = ["hearts", "spades", "clubs", "diamonds"]

cards = [(card, suit) for card in card_values for suit in suits]

def deal_card():
    card, suit = random.choice(cards)
    return str(card) + " of " + suit
    
def display_cards(dealer_cards, player_cards):
    player_hand = "You have "
    for i in range(len(player_cards)):
        player_hand += "a " + player_cards[i]
        if i >= len(player_cards) - 2 and len(player_cards) > 2:
            player_hand += ","
        player_hand += " "
        if i == len(player_cards) - 2:
            player_hand += "and "
    dealer_hand = "The dealer has "
    for i in range(len(dealer_cards)):
        dealer_hand += "a " + dealer_cards[i]
        if i < len(dealer_cards) - 1 and len(dealer_cards) > 2:
            dealer_hand += ","
        dealer_hand += " "
        if i == len(dealer_cards) - 2:
            dealer_hand += "and "
    print(player_hand)
    print(dealer_hand)
    

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


    display_cards(player_cards, dealer_cards)


round(20)