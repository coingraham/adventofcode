import numpy as np

test_secrets = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

secrets = """.##.# => #
#.#.# => #
###.. => #
##..# => #
.###. => #
.#... => #
...#. => #
#...# => #
##.## => #
..#.# => #
#.#.. => #
##... => #
.#.## => #
###.# => #"""

rules = []
for item in secrets.splitlines():
    rules.append(item.split("=>")[0].strip())

test = "#..#.#..##......###...###"
real = "#..###...#####.#.#...####.#..####..###.##.#.#.##.#....#....#.####...#....###.###..##.#....#######"


def sum_plants(curr):
    diff = (len(curr) - 100) // 2
    sum = 0
    for i, c in enumerate(curr):
        if c == '#':
            sum += (i - diff)
    return sum


if __name__ == '__main__':
    real = "...." + real + "...."
    pots_list = list(real)
    last_value = 0
    value_difference = [0]
    steady_state_count = 0

    for generation in range(1000):
        pots_list = ["".join(pots_list[x:x + 5]) for x in range(len(pots_list) - 4)]
        find_plants = np.isin(pots_list, rules)
        pots_list = "".join(np.where(find_plants == True, "#", "."))

        # Part One
        total_value = sum_plants(pots_list)
        # print(total_value)

        # Part Two
        difference = total_value - last_value
        if difference == value_difference[-1]:
            steady_state_count += 1
        if steady_state_count > 10:
            print(value_difference)
            print("Steady State for 50000000000: {}".format(((50000000000 - generation - 1) * difference) + total_value))
            break
        value_difference.append(difference)
        last_value = total_value
        pots_list = "...." + pots_list + "...."

