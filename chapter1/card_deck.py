import collections

SUIT_VALUES = dict(spades=3, hearts=2, diamonds=1, clubs=0)

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card: Card):
    """Sort by suit and rank."""
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(SUIT_VALUES) + SUIT_VALUES[card.suit]
