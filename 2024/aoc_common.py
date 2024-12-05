from functools import reduce
import operator


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


def get_8_directions():
    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
    directions.pop(4)
    return directions


def print_matrix(matrix):
    return "\n".join([" ".join(item) for item in matrix])


def remove_item_from_list_in_dictionary_value(dictionary, item):
    for k, v in dictionary.items():
        if item in v:
            dictionary[k].remove(item)

    return dictionary



