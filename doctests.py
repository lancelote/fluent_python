import doctest
import os


def load_tests(_loader, tests, _ignore):
    path = os.path.join('tests', 'chapter1', 'card_deck.doctest')
    tests.addTests(doctest.DocFileSuite(path))
    return tests
