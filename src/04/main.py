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
test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

numbers = []
boards = []
read_board = 0
current_board = []
# for i, line in enumerate(test.split("\n")):
#     if i == 0:
#         numbers = [int(n) for n in line.split(',')]
#         continue
#     if i == 1:
#         continue
#     if line.strip() == '':
#         boards.append([item for sublist in current_board for item in sublist])
#         current_board = []
#         continue
#
#     current_board.append([int(v) for v in line.split(' ') if v != ''])


with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i == 0:
            numbers = [int(n) for n in line.split(',')]
            continue
        if i == 1:
            continue
        if line.strip() == '':
            boards.append([item for sublist in current_board for item in sublist])
            current_board = []
            continue

        current_board.append([int(v) for v in line.split(' ') if v != ''])

print(boards, len(boards))

def check_board(board):
    matrix = [_ for _ in chunks(board, 5)]
    # print(matrix, transposed(matrix))
    # exit()
    for r in matrix:
        if all(x == -1 for x in r):
            return True
    for c in transposed(matrix):
        if all(x == -1 for x in c):
            return True

    return False

# Part 2
#
# no = -1
# try:
#     for draw in numbers:
#         print("drawing ",draw)
#         no = 0
#         while no < len(boards):
#             boards[no] = [-1 if x==draw else x for x in boards[no]]
#             if check_board(boards[no]):
#                 raise StopIteration
#             no += 1
# except StopIteration:
#     pass
#
# print(boards[no])
# clean = [x if x > 0 else 0 for x in boards[no]]
# print(clean)
# print(sum(clean))
# print(sum(clean) * draw)


no = -1
last_winner=None
already_won = []
try:
    for draw in numbers:
        print("drawing ",draw, already_won)
        no = 0
        while no < len(boards):
            boards[no] = [-1 if x==draw else x for x in boards[no]]
            if check_board(boards[no]) and no not in already_won:
                already_won.append(no)
                if len(already_won) == len(boards):
                    last_winner = boards[no]
                    raise StopIteration
            no += 1
except StopIteration:
    pass

print(last_winner)
clean = [x if x > 0 else 0 for x in last_winner]
print(clean)
print(sum(clean))
print(sum(clean) * draw)
