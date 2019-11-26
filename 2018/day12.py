import numpy as np


secrets = """...## => #
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

secretlines = secrets.splitlines()
plants = [x.split(" ")[0] for x in secretlines]
# print(plants)


if __name__ == '__main__':
    pots = "...#..#.#..##......###...###.."
    pots_list = list(pots)
    size = 5
    for generation in range(20):
        pots_list = ["".join(pots_list[x:x + size]) for x in range(len(pots_list) - size + 1)]
        trues = np.isin(pots_list, plants)
        pots_list = "..."
        for slot in trues:
            if slot:
                pots_list += "#"
            else:
                pots_list += "."
        pots_list += "..."
        print(pots_list)
