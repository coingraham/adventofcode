import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)

# Credit https://github.com/realasvop/advent-of-code

G = nx.DiGraph()

for line in puzzle.input_data.splitlines():
    nodes = line.split(")")
    G.add_edge(nodes[0], nodes[1])

count = 0
for node in G:
    for a in nx.ancestors(G, node):
        count += 1
print('pt1:', count)

path = nx.shortest_path_length(G.to_undirected(), source='YOU', target='SAN') - 2  # adjust to the orbited objects
print('pt2:', path)