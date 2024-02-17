import random

bank = 1000
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

def choices(dealer_cards, player_cards, bet, turn1):
    choices = {"S": "stand", "H": "hit"}
    if turn1 and bet * 2 <= bank:
        choices["D"] = "double"
    if turn1 and dealer_cards[1][0] == "ace":
        choices["I"] = "insurance"
    return choices
    
def print_choices(dealer_cards, player_cards, bet, turn1):
    print("\nPress: ")
    choice_list = choices(dealer_cards, player_cards, bet, turn1)
    for letter, move in choice_list.items():
        print("{} for {}".format(letter, move))
    print()

def value(cards):
    total = 0
    aces = 0
    for card_face, suit in cards:
        if card_face.isdigit():
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

def dealer_move(dealer_cards):
    global bank
    while True:
        if value(dealer_cards) < 17:
            print("The dealer drew a {} of {}".format(*deal_card(dealer_cards)))

            print("The dealer's new total is {}".format(value(dealer_cards)))
        else:
            break

def end_game(dealer_cards, player_cards, bet):
    global bank
    if value(dealer_cards) > value(player_cards):
        print("You lost")
        print("You lose ${}".format(bet))
        bank -= bet
    elif value(dealer_cards) < value(player_cards):
        print("You won!")
        print("You get ${}".format(bet))
        bank += bet
    elif value(dealer_cards) == value(player_cards):
        print("Push!")

def round():
    turn1 = True
    global bank
    print("You have ${}".format(bank))
    
    while True:
        bet = input("How much do you want to bet?\n")
        if bet.isdigit() and 1 <= int(bet) <= bank:
            bet = int(bet)
            break
        else:
            print("Invalid amount")

    print("\nYou bet {} dollars\n\n\n".format(bet))

    player_cards = []
    
    dealer_cards = []

    for i in range(2):
        deal_card(player_cards)
        deal_card(dealer_cards)

    while True:

        print_dealers_card(dealer_cards)

        print_player_cards(player_cards)

        print("Your total is " + str(value(player_cards)))

        if value(player_cards) == 21:
            print("\nBlackjack!")
            print("The dealer has {}".format(card_list(dealer_cards)))
            if value(dealer_cards) == 21:
                print("Push!")
            else:
                print("You win!")
                bank += bet
                print("You get ${}\n".format(bet))
            break

        print_choices(dealer_cards, player_cards, bet, turn1)

        while True:
            player_move = input().upper()
            if player_move in choices(dealer_cards, player_cards, bet, turn1).keys():
                turn1 = False
                break
            else:
                print("invalid input, try again:")

        
        match player_move:
            case "H":
                card, suit = deal_card(player_cards)
                print("\nYou got a {} of {}".format(card, suit))
                if value(player_cards) > 21:
                    print("\nYou broke!")
                    print("You lose ${}".format(bet))
                    bank -= bet
                    break
            case "S":
                print("The dealer's other card was a {} of {}".format(*dealer_cards[0]))
                dealer_move(dealer_cards)
                if value(dealer_cards) > 21:
                    print("The dealer busted!")
                    print("You won!")
                    print("You get {}".format(bet))
                    bank += bet
                end_game(dealer_cards, player_cards, bet)
                break
            case "D":
                bet *= 2
                print("\nYour bet is now ${}".format(bet))
                card, suit = deal_card(player_cards)
                print("\nYou got a {} of {}".format(card, suit))
                if value(player_cards) > 21:
                    print("You now have {}, totaling {}".format(card_list(player_cards), value(cards)))
                    print("You broke!")
                    print("You lose ${}".format(bet))
                    bank -= bet
                    break
                dealer_move(dealer_cards)
                if value(dealer_cards) > 21:
                    print("The dealer busted!")
                    print("You won!")
                    print("You get {}".format(bet))
                    bank += bet
                    break
                end_game(dealer_cards, player_cards, bet)
            case "I":
                bet2 = int(bet/2)
                if value(dealer_cards) == 21:
                    print("The dealer has Blackjack!")
                    print("You get ${}".format(bet))
                else:
                    print("The dealer does not have Blackjack")
                    print("You lose ${}".format(bet2))
                    bank -= bet2
                
        

print("------Blackjack------")
print("Insurance pays 2 to 1")
print("Blackjack pays 3 to 2\n")

while True:
    user_input = input("Would you like to play a round of Blackjack (y/n)?\n")
    if user_input == "y":
        round()
    elif user_input == "n":
        print("Come again!")
        break
    else:
        print("invalid input, try again")