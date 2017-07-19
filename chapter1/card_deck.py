"""
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')
    >>> from random import choice
    >>> choice(deck)  # doctest: +ELLIPSIS
    Card(rank='...', suit='...')
    >>> deck[:2]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
