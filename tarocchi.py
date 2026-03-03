# ~~~ TAROCCHI ~~~ #

from tarot_deck import deck
import random
import secrets
from rich.console import Console
from rich.panel import Panel

console = Console()

consent = ('Y', ' ', '')

def drawcard(response):
    hand=[]

    while True:
        if response.upper() in consent:
            if len(hand) == len(deck):
                print("***\nThe Deck Is Empty\n***")
                break
            while True:
                card_number = secrets.randbelow(78)             # or random.randint(0,77)
                card = deck[card_number]
                if card not in hand:
                    break
            hand.append(card)
            console.print(Panel(card, width=25,style="bold red"))
            response=input("Draw Again? (Y/n) ")

        else:
            return hand

header=f"{'*~~~*'} WELCOME TO TAROCCHI {'*~~~*'}"
print(header)

while True:
    hand = input("\nDraw A Card? (Y/n) ")
    if hand.upper() not in consent:
        break
    hand = drawcard(hand)
    print("***\nHere is your hand:\n")
    hand_str = "\n".join(hand)
    console.print(Panel(hand_str, width=25, title="[bright_yellow]HAND[/]", style="bold red"))
    copy = input("Print Hand for copying? Y/n ")
    if copy.upper() in consent:
        console.print(hand_str.replace("\n", ", "), style="yellow")
    #for card in hand:
    #   print(f"{"*~~~*":<} {card:^21} {"*~~~*":>}")

print("***\nThank you for playing\n***")
print("~"*len(header))

