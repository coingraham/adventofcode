from aocd.models import Puzzle
import re
puzzle = Puzzle(year=2022, day=16)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

### Reviewing code from https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py
def question1():
    # question_input = sample_input
    question_input = puzzle.input_data


    lines = [re.split('[\\s=;,]+', x) for x in question_input.splitlines()]
    G = {x[1]: set(x[10:]) for x in lines}
    F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
    I = {x: 1 << i for i, x in enumerate(F)}
    T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
    for k in T:
        for i in T:
            for j in T:
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

    def visit(v, budget, state, flow, answer):
        answer[state] = max(answer.get(state, 0), flow)
        for u in F:
            newbudget = budget - T[v][u] - 1
            if I[u] & state or newbudget <= 0: continue
            visit(u, newbudget, state | I[u], flow + newbudget * F[u], answer)
        return answer

    total1 = max(visit('AA', 30, 0, 0, {}).values())
    visited2 = visit('AA', 26, 0, 0, {})
    total2 = max(v1 + v2 for k1, v1 in visited2.items()
                 for k2, v2 in visited2.items() if not k1 & k2)
    print(total1, total2)


def question2():
    question_input = sample_input
    # question_input = puzzle.input_data

    # print(results)


if __name__ == '__main__':
    question1()
    question2()

