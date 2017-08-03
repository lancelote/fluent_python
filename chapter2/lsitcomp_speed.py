import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'


def non_ascii(char):
    return char > 127
"""


def clock(label, cmd):
    result = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in result))


clock('%-20s:' % 'list comp',
      '[ord(s) for s in symbols if ord(s) > 127]')
clock('%-20s:' % 'list comp + func',
      '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('%-20s:' % 'filter + lambda',
      'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('%-20s:' % 'filter + func',
      'list(filter(non_ascii, map(ord, symbols)))')
