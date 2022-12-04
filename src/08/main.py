#!/usr/bin/env python

import os  # NOQA
import sys  # NOQA

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re  # NOQA
import math  # NOQA
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, pairwise, combinations, combinations_with_replacement  # NOQA

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, parse_line  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8  # NOQA

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD


total = 0
result = []
table = new_table(None, width=2, height=4)
data=[]

test="""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
    # for line in test.split("\n"):
        line = line.strip()
        data.append([part.strip() for part in line.split(' | ')])


render_map = {
    0: ['a', 'b', 'c', 'e', 'f','g'],
    1: ['c', 'f'],
    2: ['a', 'c','d', 'e','g'],
    3: ['a', 'c','d', 'f','g'],
    4: ['b', 'c','d','f'],
    5: ['a', 'b', 'd','f','g'],
    6: ['a', 'b','d', 'e', 'f','g'],
    7: ['a',  'c', 'f'],
    8: ['a', 'b', 'c','d', 'e', 'f','g'],
    9: ['a', 'b', 'c','d', 'f','g'],
}

simple_digits = {'2','4','3','7', 2,4,3,7}
simple_digits_count= 0
for msg in data:
    part2 = msg[1].split(' ')
    a = [1 for s in part2 if len(s) in simple_digits]
    simple_digits_count += len(a)



"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
def get_map(scrambled: [str]):
    one = [s for s in scrambled if len(s) == 2][0]
    four = [s for s in scrambled if len(s) == 4][0]
    seven = [s for s in scrambled if len(s) == 3][0]
    eight = [s for s in scrambled if len(s) == 7][0]

    zero_or_six_or_nine = [s for s in scrambled if len(s) == 6]
    six = [pos for pos in zero_or_six_or_nine if not set(one).issubset(set(pos))][0]
    zero_or_nine = [pos for pos in zero_or_six_or_nine if set(one).issubset(set(pos))]

    two_or_three_or_five = [s for s in scrambled if len(s) == 5]
    three = [pos for pos in two_or_three_or_five if set(one).issubset(set(pos))][0]
    two_or_five = [pos for pos in two_or_three_or_five if not set(one).issubset(set(pos))]

    nine = [pos for pos in zero_or_nine if set(three).issubset(pos)][0]
    zero = [pos for pos in zero_or_nine if not set(three).issubset(pos)][0]

    two = [v for v in two_or_five if set(four).union(set(v)) == set(eight)][0]
    five = [v for v in two_or_five if set(four).union(set(v)) != set(eight)][0]

    zero = list(zero)
    one = list(one)
    two = list(two)
    three = list(three)
    four = list(four)
    five = list(five)
    six = list(six)
    seven = list(seven)
    eight = list(eight)
    nine = list(nine)

    zero.sort()
    one.sort()
    two.sort()
    three.sort()
    four.sort()
    five.sort()
    six.sort()
    seven.sort()
    eight.sort()
    nine.sort()

    return {
        "".join(zero): 0,
        "".join(one):  1,
        "".join(two): 2,
        "".join(three): 3,
        "".join(four): 4,
        "".join(five): 5,
        "".join(six): 6,
        "".join(seven): 7,
        "".join(eight): 8,
        "".join(nine): 9
    }

sum = 0
for inp in data:
    pattern = inp[0]
    signal = inp[1]

    m = get_map(pattern.split(' '))

    val = []
    for d in [list(s) for s in signal.split(' ')]:
        d.sort()
        val.append(f'{m["".join(d)]}')

    sum += int("".join(val))

print(sum)
