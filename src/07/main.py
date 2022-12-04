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
data:[int]=None
test="""16,1,2,0,4,2,7,1,2,14"""

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    data = parse_nums(f.readline())
    # for i, line in enumerate(f):
    #     line = line.strip()
    #     if line:
    #         # data.append(int(line))
    #         data.append({"line": i, "value": int(line)})

print(data)


fuel = 999999999
for i in range(len(data)):
    # for pos in data:
    _fuel = sum([math.fabs(pos - i+1) for pos in data])
    fuel = _fuel if _fuel < fuel else fuel

print(fuel)



fuel = 99999999999999999999999
for i in range(len(data)):
    # for pos in data:
    dists = [math.fabs(pos - i+1) for pos in data]
    _fuel = sum([sum(list(range(int(dist)+1))) for dist in dists])
    fuel = _fuel if _fuel < fuel else fuel

print(fuel)

