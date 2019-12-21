import sys
from heapq import *
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=18)

from collections import defaultdict
from itertools import count

# with open('inputs/18.txt') as file:
#     input = file.read()

test3 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

test = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""

input = test3

def parseInput(input):
    maze = {}
    goals = {}
    for y,row in enumerate(input.split('\n')):
        for x,cell in enumerate(row):
            p = complex(x,y)
            maze[p] = cell
            if cell in '#.': continue
            goals[cell] = p
    return maze, goals

def findLinks(maze, start):
    links = {}
    walk = defaultdict(lambda:[99999,{}])
    walk[start] = (0,set())
    next = [(start,set())]

    for step in count(1):
        if len(next)==0: break
        cur,next = next,[]
        for p,ds in cur:
            for d in [1,1j,-1,-1j]:
                c = maze[p+d]
                if c == '#' or walk[p+d][0]<=step: continue
                if c.islower():
                    links[c] = (step,ds)
                nds = ds
                if c.isupper():
                    nds = nds | {c.lower()}
                walk[p+d] = (step,nds)
                next.append((p+d,nds))
    return links # naturally sorted by distance


def findShortest1():
    maze, goals = parseInput(input)

    allKeys = {k for k in goals if k.islower()}
    links = {'@': findLinks(maze, goals['@'])}
    for k in allKeys:
        links[k] = findLinks(maze, goals[k])

    cache = {}

    def walk(name, needKeys):
        if len(needKeys) == 0:
            return 0

        key = name + ''.join(needKeys)
        if key in cache:
            return cache[key]

        shortest = float('inf')
        for k in needKeys:
            l, doors = links[name][k]
            if l >= shortest: continue  # too long to try
            if not doors.isdisjoint(needKeys): continue  # can't open doors
            tail = walk(k, needKeys - {k})
            if shortest > l + tail: shortest = l + tail
        cache[key] = shortest
        return shortest

    res = walk('@', allKeys)
    # print('cached', len(cache))
    return res

print(findShortest1())