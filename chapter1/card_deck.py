"""
>>> from random import choice

>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')

>>> deck = FrenchDeck()
>>> len(deck)
52

>>> deck[0]
Card(rank='2', suit='spades')

>>> deck[-1]
Card(rank='A', suit='hearts')


>>> choice(deck)  # doctest: +ELLIPSIS
Card(rank='...', suit='...')

>>> deck[:2]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]

>>> deck[12::13]  # Aces
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

>>> for card in deck:  # doctest: +ELLIPSIS
...     print(card)
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
...

>>> for card in reversed(deck):  # doctest: +ELLIPSIS
...     print(card)
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...

>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beasts') in deck
False

>>> for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
...     print(card)
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
...
Card(rank='A', suit='diamonds')
Card(rank='A', suit='hearts')
Card(rank='A', suit='spades')
"""

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
