# ~~~ TAROCCHI ~~~ #

from tarot_deck import deck
import random
import secrets

def drawcard(response):
    hand=[]

    while True:
        if response.upper() == 'Y':
            if len(hand) == len(deck):
                print("***\nThe Deck Is Empty\n***")
                break
            while True:
                card_number = secrets.randbelow(78)             # or random.randint(0,77)
                card = deck[card_number]
                if card not in hand:
                    break
            hand.append(card)
            print("***\nYou pulled:", card,"\n***")
            response=input("Draw Again? (Y/n)")

        else:
            return hand

header=f"{'*~~~*'} WELCOME TO TAROCCHI {'*~~~*'}"
print(header)

while True:
    hand = input("Draw A Card? (Y/n) ")
    if hand.lower() == "n":
        break
    hand = drawcard(hand)
    print("***\nHere is your hand:")
    for card in hand:
        print(f"{"*~~~*":<} {card:^21} {"*~~~*":>}")

print("***\nThank you for playing\n***")
print("~"*len(header))

