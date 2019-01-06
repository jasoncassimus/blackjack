class Card:
    suit = 'null'
    rank = 0

    def __eq__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        else:
            return False
