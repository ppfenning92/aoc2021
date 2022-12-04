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

test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            # data.append(int(line))
            data.append(list(line))

    print(data)

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

illegals = []
unfinished = []


parse = {
    "(": 1,
    ")": -1,
    "[": 1,
    "]": -1,
    "{": 1,
    "}": -1,
    "<": 1,
    ">": -1
}

processed_lines = []
for idx, line in enumerate(data):

    last_open = []
    for char in line:
        if char in list("([{<"):
            last_open.append(char)

        if char == ")":
            if last_open[-1:][0] != "(":
                illegals.append(char)
                processed_lines.append(idx)
                break
            else:
                last_open.pop()
        if char == "]":
            if last_open[-1:][0] != "[":
                illegals.append(char)
                processed_lines.append(idx)
                break
            else:
                last_open.pop()
        if char == "}":
            if last_open[-1:][0] != "{":
                illegals.append(char)
                processed_lines.append(idx)
                break
            else:
                last_open.pop()
        if char == ">":
            if last_open[-1:][0] != "<":
                illegals.append(char)
                processed_lines.append(idx)
                break
            else:
                last_open.pop()

print(illegals)
print(sum([points[il] for il in illegals]))



points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

completes = []
for idx,line in enumerate(data):
    if idx in processed_lines:
        continue
    last_open = []
    for char in line:
        if char in list("([{<"):
            last_open.append(char)

        if char == ")":
            if last_open[-1:][0] == "(":
                last_open.pop()
        if char == "]":
            if last_open[-1:][0] == "[":
                last_open.pop()
        if char == "}":
            if last_open[-1:][0] == "{":
                last_open.pop()
        if char == ">":
            if last_open[-1:][0] == "<":
                last_open.pop()

    closing = []
    for char in last_open[::-1]:
        if char == '(':
            closing.append(')')
        if char == '[':
            closing.append(']')
        if char == '{':
            closing.append('}')
        if char == '<':
            closing.append('>')

    completes.append(closing)

totals = []
for com in completes:
    sub_total = 0
    for c in com:
        sub_total *= 5
        sub_total += points[c]
    totals.append(sub_total)

totals.sort()
print(totals)

print(totals[len(totals)//2])

