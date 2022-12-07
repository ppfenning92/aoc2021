#!/usr/bin/env python
from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
from dataclasses import dataclass

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re  # NOQA
import math  # NOQA
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, pairwise, combinations, combinations_with_replacement  # NOQA

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, parse_line, pprint  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8  # NOQA

total = 0
result = []
table = new_table(None, width=2, height=4)
data=[]
test = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

@dataclass
class Cave:
    id: str
    small: bool
    neighbors: {str}
    visited: int = 0

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as file:
    for i, line in enumerate(file):
    # for i, line in enumerate(test.split('\n')):
        line = line.strip()
        if line:
            data.append(line.split('-'))


caves_net = defaultdict()
def is_small(string: str) -> bool:
    return string.islower()

for _from, _to in data:
    from_cave = caves_net[_from] if _from in caves_net else \
        caves_net.setdefault(_from, Cave(id=_from, small=is_small(_from), neighbors=set()))
    to_cave = caves_net[_to] if _to in caves_net else \
        caves_net.setdefault(_to, Cave(id=_to, small=is_small(_to), neighbors=set()))

    from_cave.neighbors.add(to_cave.id)
    to_cave.neighbors.add(from_cave.id)

paths = []


"""
    start
    /   \
c--A-----b--d
    \   /
     end
"""
# start A b A b A
def cave_can_be_visited(_path: [Cave], _cave: Cave) -> bool:

    if not _cave.small:
        return True

    if _cave.id == 'start':
        return False

    if _cave.id == 'end':
        return True

    small_in_path = [c.type_id for c in _path if c.small and c.type_id != 'start' and c.type_id != 'end']
    if _cave.id not in small_in_path:
        return True
    counts = Counter(small_in_path)
    return all(c < 2 for c in counts.values())

def find_paths(f: Cave, t: Cave, _path):

    _path.append(f)

    if f.id == t.id:
        paths.append(_path)
    else:
        for _id in f.neighbors:
            c = caves_net[_id]
            if cave_can_be_visited(_path.copy(), c):
                find_paths(c, t, _path.copy())

    # path.pop()



find_paths(caves_net['start'], caves_net['end'], [])

print(len(paths))


