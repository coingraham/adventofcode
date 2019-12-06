from collections import defaultdict
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)


# with open('input.txt') as input_file:
#     lines = input_file.readlines()

lines = puzzle.input_data.splitlines()

nodes = defaultdict(lambda: set())
for line in lines:
    a, b = line.strip().split(")")
    nodes[a].add(b)
    nodes[b].add(a)

def bfs(nodes, start):
    queue = [(start, 0)]
    seen = set()
    for node, depth in queue:
        seen.add(node)
        next_nodes = nodes.get(node, [])
        queue += [(new_node, depth + 1) for new_node in next_nodes if new_node not in seen]
        yield node, depth

print(sum(depth for node, depth in bfs(nodes, 'COM')))
print(next(depth - 2 for node, depth in bfs(nodes, 'YOU') if node == 'SAN'))