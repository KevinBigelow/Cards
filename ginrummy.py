from deck import Deck, Card
from numpy import random


class Game:
    def __init__(self, player1, player2):
        self.player1, self.player2 = Player(player1), Player(player2)

    def newhand(self):
        self.firstplay = random.choice([self.player1, self.player2])
        self.deck = Deck().shuffle()
        
        self.discard = [].append(self.deck.draw())


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.played = []
        self.points = 0

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
            return self.hand.remove(Card(rank, suit))



