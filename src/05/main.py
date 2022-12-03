#!/usr/bin/env python

import os  # NOQA
import sys  # NOQA

import os, sys
from functools import total_ordering

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
test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

test_result = """
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111...."""

@total_ordering
class Point:
    """Simple 2-dimensional point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle(self, to=None):
        if to is None:
            return math.atan2(self.y, self.x)
        return math.atan2(self.y - to.y, self.x - to.x)

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def neighbours_4(self):
        return [self + p for p in DIRS_4]

    def neighbours_8(self):
        return [self + p for p in DIRS_8]


data: list[tuple[Point,Point]] =[]
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split("\n")):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            x, y = tuple(line.split(' -> '))
            data.append(
                (
                    Point(*parse_nums(x)),
                    Point(*parse_nums(y))
                )
            )

# print(data)

max_x = max_y = 0
for start, end in data:
    if start.x > max_x:
        max_x = start.x
    if end.x > max_x:
        max_x = start.x
    if start.y > max_y:
            max_y = start.y
    if end.y > max_y:
        max_y = start.y

# print(max_x, max_y)

table = new_table(0, width=max_x+1, height=max_y+1)

for v in data:
    start, end =v

    # Part1
    # if start.x == end.x:
    #     print(start.x, '| ',start.y, end.y)
        # for col in range(min(start.y, end.y),max(start.y, end.y) +1 ):
        #     table[col][start.x] += 1
        # continue
    # if start.y == end.y:
    #     print(start.x, end.x,  '--', start.y)
        # for row in range(min(start.x, end.x),max(start.x, end.x) +1 ):
        #     table[start.y][row] += 1
        # continue

    # Part 2
    if True or math.fabs(math.degrees(start.angle(end))) % 45.0 == 0:
    # if start.x == end.y and start.y == end.x:
        dx = 0 if start.x == end.x else 1 if start.x < end.x else -1
        dy = 0 if start.y == end.y else 1 if start.y < end.y else -1

        diag = []
        step = start
        while step != end:
            diag.append(step)
            step += Point(dx, dy)
        diag.append(end)
        print(diag)
        for p in diag:
            table[p.y][p.x] += 1

crit = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        cell = table[i][j]
        if cell >= 2:
            crit += 1
        table[i][j] = f"{'.' if cell == 0 else cell}"

print_grid(table)
print(crit)


