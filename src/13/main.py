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
data=[]

test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
points = []
folds = []
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    coords = True
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            if coords:
                points.append(Point(*parse_nums(line)))
            else:
                line = line.replace('fold along ', '')
                folds.append(line.split('='))
        else:
            coords = False

y_max = 0
x_max = 0
for point in points:
    x_max = point.x if point.x > x_max else x_max
    y_max = point.y if point.y > y_max else y_max

table = new_table('.', width=x_max+1, height=y_max+1)
for point in points:
    table[point.y][point.x] = '#'

print_grid(table)

def get_mark(str1: str, str2: str):
    if str1 == '#' or str2 == '#':
        return '#'
    return '.'

def fold_left(l):
    left = [row[:l] for row in table]
    right = [row[l+1:][::-1] for row in table]


    for i in range(len(right)):
        for j in range(len(right[i])):
            left[i][j] = get_mark(left[i][j], right[i][j])

    return left

def fold_up(l):
    top = table[:l]
    bot = table[l+1:]

    bot = bot[::-1]

    for i in range(len(bot)):
        for j in range(len(bot[i])):
            top[i][j] = get_mark(top[i][j], bot[i][j])

    return top

import numpy as np
# for dir, lin in folds[:1]:
for dir, lin in folds:
    if dir == 'y':
        table = fold_up(int(lin))
    if dir == 'x':
        table = fold_left(int(lin))
    print('')
    print_grid(table)


    flattened = str(list(np.array(table).flat).count('#'))
    if len(flattened) == 8:
        print(flattened)
