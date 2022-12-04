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

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, mul, parse_line  # NOQA
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
test="""2199943210
3987894921
9856789892
8767896789
9899965678"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for line in test.split('\n'):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            # data.append(int(line))
            data.append([int(x) for x in list(line)])

print(data)


def check_index(i,j):
    return 0 <= i < len(data) and 0 <= j < len(data[i])
def get_neighbors(i,j):
    right = data[i][j+1] if  check_index(i,j+1)  else None
    left = data[i][j-1] if  check_index(i,j-1)  else None
    top = data[i-1][j] if  check_index(i-1,j)  else None
    bottom = data[i+1][j] if  check_index(i+1,j)  else None

    return top, right, bottom, left




lows = []
for row in range(len(data)):
    for col in range(len(data[row])):
        neighbors = list(x for x in get_neighbors(row,col) if x != None)
        if all(data[row][col] < n for n in neighbors):
            lows.append(data[row][col] + 1)

print(sum(lows))


import numpy as np
from scipy import ndimage

data_2 = data
for row in range(len(data_2)):
    for col in range(len(data_2[row])):
        data_2[row][col] = 0 if data_2[row][col] == 9 else 1


heatmap = np.array(data)

highlighted_islands, num_features = ndimage.label(heatmap)

islands = []
for i in range(num_features):
    island_size=0
    for row in range(len(highlighted_islands)):
        for col in range(len(highlighted_islands[row])):
            if highlighted_islands[row][col] == i+1:
                island_size+=1
    islands.append(island_size)

islands.sort(reverse=True)
res = 1
for v in islands[0:3]:
    res *= v
print(res)


