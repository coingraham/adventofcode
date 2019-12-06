import aoc_common as ac
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)

# print(puzzle.input_data)

orbits = puzzle.input_data.splitlines()

test2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

# orbits = test2.splitlines()

orbits = [x.split(")") for x in orbits]

direct = len(orbits)
search_letters = ["XX6"]
indirect = 0
level = 0


def search_orbits(search, orbits):
    connections = []
    for orbit in orbits:
        for s in search:
            if orbit[0] == s:
                connections.append(orbit[1])

    return connections


def single_search_orbits(search, orbits):
    for orbit in orbits:
        if orbit[0] == search:
            return orbit[1]


# Part One
while search_letters:
    indirect += level * len(search_letters)
    level += 1
    search_letters = search_orbits(search_letters, orbits)
print(direct + indirect)


# Part Two
orbits_backwards = [[x[1], x[0]] for x in orbits]

you = ["YOU"]
san = ["SAN"]

while True:
    new = single_search_orbits(you[-1], orbits_backwards)
    if new:
        you.append(new)
    else:
        break

while True:
    new = single_search_orbits(san[-1], orbits_backwards)
    if new:
        san.append(new)
    else:
        break

print(len(list(set(you) & set(san))))
print("{}_{}".format(you, len(you)))
print("{}_{}".format(san, len(san)))

print(len(you) - 1 + len(san) - 1 - (len(list(set(you) & set(san)))*2))
