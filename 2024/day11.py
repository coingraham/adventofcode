from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=11)

sample_data = '''125 17'''

# q_i = [int(n) for n in sample_data.split()]
q_i = [int(n) for n in puzzle.input_data.split()]


def part_one(q_i, times):
    import copy
    old = q_i

    while times:
        process_list = copy.deepcopy(old)
        old = []

        for item in process_list:
            # rule 1
            if item == 0:
                old.append(1)
                continue

            # rule 2
            digit_list = [int(d) for d in str(item)]
            if len(digit_list) % 2 == 0:
                half_index = (len(digit_list) // 2)
                old.append(int(''.join(map(str, digit_list[:half_index]))))
                old.append(int(''.join(map(str, digit_list[half_index:]))))
                continue

            # rule 3
            old.append(item * 2024)

        times -= 1

    return len(old)


def part_two(q_i, times):
    from collections import defaultdict
    old = defaultdict(int)
    for i in q_i:
        old[i] = 1

    while times:
        process_dict = old.copy()
        old = defaultdict(int)
        for key, count in process_dict.items():
            # rule 1
            if key == 0:
                old[1] += count
                continue

            # rule 2
            digit_list = [int(d) for d in str(key)]
            if len(digit_list) % 2 == 0:
                half_index = (len(digit_list) // 2)
                first_half = int(''.join(map(str, digit_list[:half_index])))
                last_half = int(''.join(map(str, digit_list[half_index:])))
                old[first_half] += count
                old[last_half] += count
                continue

            # rule 3
            old[key * 2024] += count

        times -= 1

    return sum(list(old.values()))


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    print(part_one(q_i, 25))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function took {execution_time:.6f} seconds to execute")

    start_time = time.perf_counter()
    print(part_two(q_i, 75))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function took {execution_time:.6f} seconds to execute")
