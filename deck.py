from numpy import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        print(self.rank, "of", self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["clubs", "hearts", "diamonds", "spades"]:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop(0)
        return card
