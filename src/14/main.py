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


test = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

# result = "NNCB"
result = "ONSVVHNCFVBHKVPCHCPV"
data = {}
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            key, val = line.split(' -> ')
            data[key] = val

# for step in range(10):
#     temp = list(result)
#     print(temp)
#     it = 1
#     for i, pair in enumerate(pairwise(result)):
#         pair = list(pair)
#         temp.insert(i+it, data["".join(pair)])
#         it += 1
#
#     result = ''.join(temp)
#     print(step+1, result)
#
# print(len(result))
# counts = Counter(list(result))
# print(counts)
# print(max(counts.values()) - min(counts.values()))


#  https://www.reddit.com/r/adventofcode/comments/rg5h8e/2021_day_14_visualization_with_a_chart/
state = {}
def update_state(key: str, amount = 1):
    if key in state:
        state[key] += amount
    else:
        state[key] = amount

counter = Counter(result)
letters = dict(counter)

for pair in pairwise(list(result)):
    key = "".join(pair)
    update_state(key)

print('init', state)
for step in range(40):
    current_keys = list(state.keys())
    updates = []
    for gen in current_keys:
        amount = state[gen]

        inserted_letter = data[gen]

        one, two = list(gen)
        key1 = f"{one}{inserted_letter}"
        key2 = f"{inserted_letter}{two}"
        # print(gen, inserted_letter, key1, key2, amount)

        updates.append((key1,key2,amount))

        if inserted_letter in letters:
            letters[inserted_letter] += amount
        else:
            letters[inserted_letter] = amount

        del state[gen]

    # print(state)

    for key1,key2,amount in updates:
        update_state(key1, amount)
        update_state(key2, amount)


print(letters)
print(max(letters.values())-min(letters.values()))
