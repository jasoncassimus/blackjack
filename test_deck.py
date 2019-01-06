import unittest
from card import Card
from deck import Deck


class CreateDeckTest(unittest.TestCase):
    def test_shuffle(self):
        d = Deck()
        d.shuffle()
        for suit in ['heart', 'diamond', 'spade', 'club']:
            for rank in range(1,14):
                c = Card()
                c.suit = suit
                c.rank = rank
                self.assertTrue(d.cards.__contains__(c))

