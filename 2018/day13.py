import numpy as np
import day13_input as d13
import itertools


def print_paths(paths):
    for array in paths:
        print("".join(array))


def find_north_south_east_west(carts):
    carts = build_cart_map(carts, ">", "east", np.where(paths == ">"))
    carts = build_cart_map(carts, "^", "north", np.where(paths == "^"))
    carts = build_cart_map(carts, "<", "west",np.where(paths == "<"))
    carts = build_cart_map(carts, "v", "south",np.where(paths == "v"))
    return carts


def build_cart_map(carts, symbol, direction, locations):
    if len(locations) > 0:
        for i in range(len(locations[0])):
            new_id = carts[id][-1] + 1
            new_id_name = "cart_{}".format(str(new_id))
            carts[id].append(new_id)
            carts[new_id_name] = {
                "symbol": symbol,
                "direction": direction,
                "location": [locations[0][i], locations[1][i]],
                "toggle": itertools.cycle(['left', 'straight', 'right'])
            }
        return carts


path_lines = d13.sample.splitlines()

original = []
for line in path_lines:
    line_list = list(line)
    original.append(line_list)


paths = np.array(original, np.chararray)
print_paths(paths)

carts = {id: [0]}

carts = find_north_south_east_west(carts)
print(carts)









# identify all carts - initial location and direction - replacement space - toggle turning

# loop through carts, moving them

# create move north, south, east, west, intersection, corner, crash logic