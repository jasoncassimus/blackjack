from card import Card
import random

class Deck:
    cards = []

    def shuffle(self):
        for suit in ['heart', 'diamond', 'spade', 'club']:
            for rank in range(1,14):
                c = Card()
                c.suit = suit
                c.rank = rank
                self.cards.append(c)

        random.shuffle(self.cards)


    def deal(self, player):
        


"""
d = Deck()
d.shuffle()
for x in d.cards:
    print(str(x.rank) + " of " + str(x.suit))
"""
