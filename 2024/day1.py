from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=1)

sample_data = '''3   4
4   3
2   5
1   3
3   9
3   3'''

# question input
# q_i = [n for n in sample_data.splitlines()]
q_i = [n for n in puzzle.input_data.splitlines()]

def part_one():
    list1, list2 = [], []
    for item in q_i:
        i, j = item.split()
        list1.append(int(i))
        list2.append(int(j))

    list1.sort()
    list2.sort()

    result = sum(map(lambda x: abs(x[0] - x[1]), zip(list1, list2)))

    return result


def part_two():
    list1, list2 = [], []
    for item in q_i:
        i, j = item.split()
        list1.append(int(i))
        list2.append(int(j))

    similarity_score = 0
    for x in list1:
        x_count = list2.count(x)
        similarity_score += x * x_count

    return similarity_score


if __name__ == '__main__':
    print(part_one())
    print(part_two())
