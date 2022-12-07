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
test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            # data.append(int(line))
            data.append( [int(x) for x in list(line)])

# print(data)


import numpy as np
# data = [[8]]
_data = np.array(data)


SIZE_X = len(data[0])
SIZE_Y = len(data)
data = np.tile(_data, (5, 5))

for i in range(0,5):


    for j in range(0,5):
        if i == j == 0:
            continue
        x_start = i*SIZE_X
        x_end = x_start + SIZE_X
        y_start = j*SIZE_Y
        y_end = y_start + SIZE_Y

        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                mod = (data[x][y] + i + j) % 9
                data[x][y] = mod if mod > 0 else 9



print_grid(data, lambda x: f"{x} ")
# ta = """8 9 1 2 3
# 9 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7"""
# assert(np.array_equal(map, np.array([list(s) for s in ta.split('\n')])))
#
#
# ass = """11637517422274862853338597396444961841755517295286
# 13813736722492484783351359589446246169155735727126
# 21365113283247622439435873354154698446526571955763
# 36949315694715142671582625378269373648937148475914
# 74634171118574528222968563933317967414442817852555
# 13191281372421239248353234135946434524615754563572
# 13599124212461123532357223464346833457545794456865
# 31254216394236532741534764385264587549637569865174
# 12931385212314249632342535174345364628545647573965
# 23119445813422155692453326671356443778246755488935
# 22748628533385973964449618417555172952866628316397
# 24924847833513595894462461691557357271266846838237
# 32476224394358733541546984465265719557637682166874
# 47151426715826253782693736489371484759148259586125
# 85745282229685639333179674144428178525553928963666
# 24212392483532341359464345246157545635726865674683
# 24611235323572234643468334575457944568656815567976
# 42365327415347643852645875496375698651748671976285
# 23142496323425351743453646285456475739656758684176
# 34221556924533266713564437782467554889357866599146
# 33859739644496184175551729528666283163977739427418
# 35135958944624616915573572712668468382377957949348
# 43587335415469844652657195576376821668748793277985
# 58262537826937364893714847591482595861259361697236
# 96856393331796741444281785255539289636664139174777
# 35323413594643452461575456357268656746837976785794
# 35722346434683345754579445686568155679767926678187
# 53476438526458754963756986517486719762859782187396
# 34253517434536462854564757396567586841767869795287
# 45332667135644377824675548893578665991468977611257
# 44961841755517295286662831639777394274188841538529
# 46246169155735727126684683823779579493488168151459
# 54698446526571955763768216687487932779859814388196
# 69373648937148475914825958612593616972361472718347
# 17967414442817852555392896366641391747775241285888
# 46434524615754563572686567468379767857948187896815
# 46833457545794456865681556797679266781878137789298
# 64587549637569865174867197628597821873961893298417
# 45364628545647573965675868417678697952878971816398
# 56443778246755488935786659914689776112579188722368
# 55172952866628316397773942741888415385299952649631
# 57357271266846838237795794934881681514599279262561
# 65719557637682166874879327798598143881961925499217
# 71484759148259586125936169723614727183472583829458
# 28178525553928963666413917477752412858886352396999
# 57545635726865674683797678579481878968159298917926
# 57944568656815567976792667818781377892989248891319
# 75698651748671976285978218739618932984172914319528
# 56475739656758684176786979528789718163989182927419
# 67554889357866599146897761125791887223681299833479"""
# assert(np.array_equal(map, np.array([list(s) for s in ass.split('\n')])))

map = np.array(data)


maxnum=9
min_val, max_val = 1, len(data)
map[0,0]=0
map[max_val-1,max_val-1]=0


#Initialize auxiliary arrays
distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
distmap[0,0]=0
originmap=np.ones((max_val,max_val),dtype=int)*np.nan
visited=np.zeros((max_val,max_val),dtype=bool)
finished = False
x,y=int(0),int(0)
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
    # move to x+1,y
    if x < max_val-1:
        if distmap[x+1,y]>map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
            distmap[x+1,y]=map[x+1,y]+distmap[x,y]
            originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x-1,y
    if x>0:
        if distmap[x-1,y]>map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
            distmap[x-1,y]=map[x-1,y]+distmap[x,y]
            originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x,y+1
    if y < max_val-1:
        if distmap[x,y+1]>map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
            distmap[x,y+1]=map[x,y+1]+distmap[x,y]
            originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x,y-1
    if y>0:
        if distmap[x,y-1]>map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
            distmap[x,y-1]=map[x,y-1]+distmap[x,y]
            originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))

    visited[x,y]=True
    dismaptemp=distmap
    dismaptemp[np.where(visited)]=np.Infinity
    # now we find the shortest path so far
    minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
    x,y=minpost[0],minpost[1]
    if x==max_val-1 and y==max_val-1:
        finished=True
    count=count+1

#Start backtracking to plot the path
mattemp=map.astype(float)
x,y=max_val-1,max_val-1
path=[]
mattemp[int(x),int(y)]=np.nan

while x>0.0 or y>0.0:
    path.append([int(x),int(y)])
    xxyy=np.unravel_index(int(originmap[int(x),int(y)]), (max_val,max_val))
    x,y=xxyy[0],xxyy[1]
    mattemp[int(x),int(y)]=np.nan
path.append([int(x),int(y)])


print('The path length is: '+str(int(distmap[max_val-1,max_val-1] )+  data[len(data)-1][len(data[0])-1]))
print('The dump/mean path should have been: '+str(maxnum*max_val))
