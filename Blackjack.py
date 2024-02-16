import random

cards = list(range(2, 11)) + ["Jack", "King", "Queen", "Ace"]
signs = ["hearts", "spades", "clubs", "diamonds"]

def deal_card():
    return str(cards[random.randint(0, 12)]) + " of " + signs[random.randint(0, 3)]
    
def round(bank):
    print("You have ${}".format(bank))
    bet = input("How much do you want to bet?\n")

    def bet_to_int(bet):
        try:
            bet = int(bet)
            return True
        except ValueError:
            return False

    while not bet_to_int(bet) or int(bet) < 1 or int(bet) > bank:
        print("Invalid amount")
        bet = input("Try again: ")

    print("You bet {} dollars".format(bet))

round(20)