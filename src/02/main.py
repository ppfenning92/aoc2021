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

depth = 0
x = 0
aim = 0 # part 2

table = new_table(None, width=2, height=4)
data=[]

dirs = {
    "forward": 1, "up": -1, "down": 1
}

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(tuple(line.split()))


for dir, val in data:
    val = int(val) * dirs[dir]
    if dir == "forward":
        x += val
        depth += aim * val # part 2
    if dir == "up" or dir == "down":
        # depth  += val
        aim  += val # part 2

print("depth:", depth)
print("x:", x)

print("res", depth * x)
