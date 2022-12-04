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
test="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

# test = """11111
# 19991
# 19191
# 19991
# 11111"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for _, line in enumerate(test.split('\n')):
    for _, line in enumerate(f):
        line = line.strip()
        if line:
            data.append([int(x) for x in list(line)])

    print(data)


def check_index(i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[i])
def get_adjacent(i, j):
    top = (i-1,j) if  check_index(i-1,j)  else None
    top_right = (i-1,j+1) if  check_index(i-1,j+1)  else None
    right = (i,j+1) if  check_index(i,j+1)  else None
    bottom_right = (i+1,j+1) if  check_index(i+1,j+1)  else None
    bottom = (i+1,j) if  check_index(i+1,j)  else None
    bottom_left = (i+1,j-1) if  check_index(i+1,j-1)  else None
    left = (i,j-1) if  check_index(i,j-1)  else None
    top_left = (i-1,j-1) if  check_index(i-1,j-1)  else None

    return top, top_right, right, bottom_right, bottom, bottom_left, left, top_left

print(get_adjacent(1,1))


flashes = 0
flashed = set()
def flash(i,j):
    global flashes
    if (i, j) not in flashed:
        flashes += 1
        flashed.add((i,j))

        adj = [tup for tup in get_adjacent(i,j) if tup]
        for r,c in [tup for tup in adj if tup]:
            data[r][c] += 1
            if data[r][c] > 9:
                flash(r, c)


for day in range(100000):
    flashed = set()

    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] += 1

    for row in range(len(data)):
        for col in range(len(data[row])):

            if data[row][col] > 9:
                flash(row,col)




    for row,col in flashed:
        data[row][col] = 0

    if len(flashed) == len(data) * len(data[0]):
        print('all', day +1)
        break



print(flashes)

