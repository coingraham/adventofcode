from functools import reduce
import math
import operator


def get_sum_of_array(array):
    return reduce((lambda x, y: x + y), array)


def get_max_key_of_dictionary(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


def get_max_value_of_dictionary(dictionary):
    return max(dictionary.values())


def get_matrix(x, y):
    return [[j for j in range(x)] for i in range(y)]


def remove_item_from_list_in_dictionary_value(dictionary, item):
    for k, v in dictionary.items():
        if item in v:
            dictionary[k].remove(item)

    return dictionary

import itertools
# toggle = itertools.cycle(['red', 'green', 'blue']).next
# toggle()

import parse
pr = parse.compile("{} => {}")
# for l in ls:
#     r = pr.parse(l)
#     rules[r[0]] = r[1]

# Functions for 2019
def get_fuel_for_module(module):
    # return (math.floor(module / 3)) - 2
    return module // 3 - 2


def get_fuel_for_fuel(fuel):
    current_fuel = math.floor(fuel / 3) - 2
    if current_fuel < 1:
        return 0
    else:
        return current_fuel + get_fuel_for_fuel(current_fuel)


def map_reduce_fuel(module_list):
    return reduce(operator.add, map(lambda x: x // 3 - 2 if x > 6 else 0, module_list))


def mr_fuel_for_fuel(fuel_list):
    return reduce(operator.add, map(lambda x: get_fuel_for_fuel(x), fuel_list))


def get_intcode(test, i, j):
    test[1] = i
    test[2] = j
    for tranche in [(test[x:x + 4]) for x in range(0, len(test) - 3, 4)]:
        if tranche[0] == 1:
            test[tranche[3]] = test[tranche[1]] + test[tranche[2]]
        if tranche[0] == 2:
            test[tranche[3]] = test[tranche[1]] * test[tranche[2]]
        if tranche[0] == 99:
            return test[0]
