from deck import Deck, Card


class Discard:
    def __init__(self):
        self.cards = []
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.played = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def play(self):
        pass

    def discard(self, rank, suit):
        if Card(rank, suit) in self.hand:



