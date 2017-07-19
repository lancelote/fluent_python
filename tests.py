import doctest

import chapter1.card_deck


def load_tests(_loader, tests, _ignore):
    tests.addTests(doctest.DocTestSuite(chapter1.card_deck))
    return tests
