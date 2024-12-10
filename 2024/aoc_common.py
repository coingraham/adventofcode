from collections import defaultdict
from functools import reduce
import operator
import collections as col


def get_sum_of_array(array):
    return reduce((lambda x, y: x + y), array)


def get_max_key_of_dictionary(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


def get_max_value_of_dictionary(dictionary):
    return max(dictionary.values())


def get_matrix(x, y):
    return [[j for j in range(x)] for i in range(y)]


def build_2_d(string_input):
    return [list(j) for j in string_input.splitlines()]


def build_2_d_ints(string_input):
    return [list(map(int, j)) for j in string_input.splitlines()]


def identify_locations(mapping):
    identities = defaultdict(list)
    for j, row in enumerate(mapping):
        for i, column in enumerate(row):
            identities[column].append((j, i))

    return identities


def get_8_directions():
    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
    directions.pop(4)
    return directions


def print_matrix(matrix):
    print("\n".join([" ".join(item) for item in matrix]))


def remove_item_from_list_in_dictionary_value(dictionary, item):
    for k, v in dictionary.items():
        if item in v:
            dictionary[k].remove(item)

    return dictionary



from multiprocessing import Pool
from os import cpu_count

def function_to_call(iter):
    return 0

def part_one(list_to_iterate):
    threads = max(cpu_count() - 1, 1)
    sum_of_thing = 0

    with Pool(threads) as pool:
        for values in pool.imap_unordered(function_to_call, list_to_iterate):
                sum_of_thing += values

    return sum_of_thing



