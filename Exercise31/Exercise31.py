import random

for cards in range (1,5):
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)
    print()