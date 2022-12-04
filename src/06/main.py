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
data=None

test="""3,4,3,1,2"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # data = parse_nums(test)
    data = parse_nums(f.readline())
    # for i, line in enumerate(f):
    #     line = line.strip()
    #     if line:


def day(val: int):
    val -= 1
    return val if val >= 0 else 6

result = data
for d in range(1,81):
    new = result.count(0)
    result = [day(fish) for fish in result]
    if new > 0:
        result.extend([8]*new)

# assert len(result) == 5934
print("part 1:", len(result))

result = data

state = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0
}
for fish in data:
    state[fish] += 1

print(state)

for d in range(1,257):
    state = {
        0: state[1],
        1: state[2],
        2: state[3],
        3: state[4],
        4: state[5],
        5: state[6],
        6: state[7] + state[0],
        7: state[8],
        8: state[0]
    }

    print(state)

print(sum(state.values()))

# assert len(result) == 26984457539




