#!/usr/bin/env python
from __future__ import annotations
import os  # NOQA
import sys  # NOQA

import os, sys
from dataclasses import dataclass, field
from typing import Optional

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

hex_to_bin = {}
bin_to_hex = {}
bin_hex = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111"""

# tests = [
#     ('D2FE28', 2021 ),
#     ('38006F45291200', None),
#     ('EE00D40C823060', None)
#     # ('8A004A801A8002F478', 16),
#     # ('620080001611562C8802118E34', 12),
#     # ('C0015000016115A2E0802F182340', 23)
# ]
# data = "D2FE28"
# data = "38006F45291200"
# data = "EE00D40C823060"


# data = "8A004A801A8002F478"
# data = "620080001611562C8802118E34"
# data = "C0015000016115A2E0802F182340"
# data = "A0016C880162017C3686B18A3D4780"



# data = "C200B40A82" # finds the sum of 1 and 2, resulting in the value 3.
# data = "04005AC33890" # finds the product of 6 and 9, resulting in the value 54.
# data = "880086C3E88112" # finds the minimum of 7, 8, and 9, resulting in the value 7.
# data = "CE00C43D881120" # finds the maximum of 7, 8, and 9, resulting in the value 9.
# data = "D8005AC2A8F0" # produces 1, because 5 is less than 15.
# data = "F600BC2D8F" # produces 0, because 5 is not greater than 15.
# data = "9C005AC2F8F0" # produces 0, because 5 is not equal to 15.
# data = "9C0141080250320F1802104A08" #produces 1, because 1 + 3 = 2 * 2.
data = "2052ED9802D3B9F465E9AE6003E52B8DEE3AF97CA38100957401A88803D05A25C1E00043E1545883B397259385B47E40257CCEDC7401700043E3F42A8AE0008741E8831EC8020099459D40994E996C8F4801CDC3395039CB60E24B583193DD75D299E95ADB3D3004E5FB941A004AE4E69128D240130D80252E6B27991EC8AD90020F22DF2A8F32EA200AC748CAA0064F6EEEA000B948DFBED7FA4660084BCCEAC01000042E37C3E8BA0008446D8751E0C014A0036E69E226C9FFDE2020016A3B454200CBAC01399BEE299337DC52A7E2C2600BF802B274C8848FA02F331D563B3D300566107C0109B4198B5E888200E90021115E31C5120043A31C3E85E400874428D30AA0E3804D32D32EED236459DC6AC86600E4F3B4AAA4C2A10050336373ED536553855301A600B6802B2B994516469EE45467968C016D004E6E9EE7CE656B6D34491D8018E6805E3B01620C053080136CA0060801C6004A801880360300C226007B8018E0073801A801938004E2400E01801E800434FA790097F39E5FB004A5B3CF47F7ED5965B3CF47F7ED59D401694DEB57F7382D3F6A908005ED253B3449CE9E0399649EB19A005E5398E9142396BD1CA56DFB25C8C65A0930056613FC0141006626C5586E200DC26837080C0169D5DC00D5C40188730D616000215192094311007A5E87B26B12FCD5E5087A896402978002111960DC1E0004363942F8880008741A8E10EE4E778FA2F723A2F60089E4F1FE2E4C5B29B0318005982E600AD802F26672368CB1EC044C2E380552229399D93C9D6A813B98D04272D94440093E2CCCFF158B2CCFE8E24017CE002AD2940294A00CD5638726004066362F1B0C0109311F00424CFE4CF4C016C004AE70CA632A33D2513004F003339A86739F5BAD5350CE73EB75A24DD22280055F34A30EA59FE15CC62F9500"

for _map in bin_hex.split('\n'):
    _hex, _bin = _map.split(' = ')
    hex_to_bin[_hex] = _bin
    bin_to_hex[_bin] = _hex

part1 = []
bits = "".join([hex_to_bin[_h] for _h in list(data)])


def get_n(n: int):
    global bits
    first_n = bits[:n]
    bits = bits[n:]
    return first_n

def ver_type():
    return int(get_n(3), 2), int(get_n(3), 2)

def literal():
    parse5 = True
    group = 1
    groups = ''
    while parse5:
        _ = get_n(5)
        pre = _[0]
        gr = _[1:]
        groups += "".join(gr)
        group += 1
        if pre == '0':
            parse5 = False
    return int(groups, 2)


part2 = []

def mul(vals: [int]):
    res = 1
    for val in vals:
        res *= val
    return res
def parse():
    version, type_id = ver_type()
    # print(type_id)
    # part1.append(version)
    if type_id == 4:
        part2.append(literal())
    else:
        part2.append(f"{type_id}")
        op = int(get_n(1),2)
        if op == 1:
            times = int(get_n(11), 2)
            for i in range(times):
                parse()
        if op == 0:
            next_bits = int(get_n(15), 2)
            current_length = len(bits)
            while len(bits) > current_length - next_bits:
                parse()


parse()
@dataclass
class OpTree:
    op: Optional[str]
    val: Optional[int]
    parent: Optional[OpTree]
    children: [OpTree] = field(default_factory=list)

    def __repr__(self):
        return f"{self.op}"
tree = OpTree(op=part2[0], parent=None, val=None)
current_op = [tree]
def resolve_operator_tree():
    # for _ in part2[1:]:
    #     curr = current_op[len(current_op)-1]
    #     if type(_) == str:
    #         new_op = OpTree(op=_, parent=curr, val=None)
    #         curr.children.append(new_op)
    #         current_op.append(new_op)
    #     else:
    #         new_val = OpTree(val=_, parent=curr, op=None)
    #         curr.children.append(new_val)
    global part2
    part2.reverse()
    resolved_ops = 1
    vals = []
    index = 0
    # while len(part2) > 6:
    for i in range(15):
        print(part2)
        val_or_op = part2[index]
        print(val_or_op, index)
        index += 1
        if type(val_or_op) == str:
            if val_or_op == '0':
                part2 = [sum(vals)] + part2[index:]
            if val_or_op == '1':
                part2 = [mul(vals)] + part2[index:]
            if val_or_op == '2':
                part2 = [min(vals)] + part2[index:]
            if val_or_op == '3':
                part2 = [max(vals)] + part2[index:]
            if val_or_op == '5':
                val1, val2 = vals
                part2 = [1 if val1 > val2 else 0] + part2[index:]
            if val_or_op == '6':
                val1, val2 = vals
                part2 = [1 if val1 < val2 else 0] + part2[index:]
            if val_or_op == '7':
                val1, val2 = vals
                part2 = [1 if val1 == val2 else 0] + part2[index:]

            vals = []
            index = resolved_ops
            resolved_ops += 1
        else:
            vals.append(val_or_op)

    #

#
#


# print(bits)
# print(part1)
# print(sum(part1))
# resolve_operator_tree()
part2.reverse()
print(part2)
