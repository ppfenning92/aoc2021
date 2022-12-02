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

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, parse_line, transpose  # NOQA
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
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(list(line))

# part 1
#
# gamma = []
# epsilon = []
# for pos in transposed(data):
#     counter = Counter(pos)
#     m = counter.most_common(1)[0][0]
#     l = "1" if m == "0" else "0"
#     gamma.append(m)
#     epsilon.append(l)
#
# print(gamma, epsilon)
# gamma = "0b" + "".join(gamma)
# epsilon = "0b" + "".join(epsilon)
#
# print(gamma, epsilon)
# print(int(gamma, 2), int(epsilon, 2))
# print(int(gamma, 2) * int(epsilon, 2))

# data = [
# list('00100'),
# list('11110'),
# list('10110'),
# list('10111'),
# list('10101'),
# list('01111'),
# list('00111'),
# list('11100'),
# list('10000'),
# list('11001'),
# list('00010'),
# list('01010'),
# ]
print(transposed(data))
def get_most_and_least_at_pos(d, pos, choose_lower=False):
    _d = transposed(d)[pos]
    counter = Counter(_d)
    print(counter)
    m = counter.most_common(1)[0][0]
    l = "1" if m == "0" else "0"
    print("m",m, 'len', len(_d), 'pos', pos)
    if counter.get('1') == counter.get('0'):
        if choose_lower:
            l = '0'
        else:
            m = '1'
    return m,l

oxy_copy = data
co2_copy = data
p = 0
while len(oxy_copy) > 1:
    m,l = get_most_and_least_at_pos(oxy_copy, p)
    print('oxy', len(oxy_copy), p, m)
    oxy_copy = [entry for entry in oxy_copy if entry[p] == m]
    p += 1


p = 0
while len(co2_copy) > 1:
    m, l = get_most_and_least_at_pos(co2_copy, p, True)
    print('co2', len(co2_copy), p, l)
    co2_copy = [entry for entry in co2_copy if entry[p] == l]
    p += 1

print(oxy_copy, co2_copy)
oxygen = int("".join(oxy_copy[0]),2)
co2 = int("".join(co2_copy[0]),2)

print(oxygen*co2)
