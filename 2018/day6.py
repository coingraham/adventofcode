import day6_input as d6
import operator

def get_manhatten_closest(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))

def find_closest(coord):
    closest_distance = d6.max_plane
    closest_name = ""
    dot = False
    for k, v in d6.coords_dictionary.items():
        distance = get_manhatten_closest(coord, v)
        if distance == closest_distance:
            dot = True
        if distance < closest_distance:
            closest_distance = distance
            closest_name = k
            dot = False

    if dot:
        return "."
    else:
        return closest_name


def get_outer_edges(space_plan):
    remove_list = []

    remove_list.extend(space_plan[0])
    remove_list.extend(space_plan[-1])

    for row in space_plan:
        remove_list.append(row[0])
        remove_list.append(row[-1])

    return set(remove_list)


def part_one_build_space_and_walk():

    space = [[j for j in range(d6.max_plane)] for i in range(d6.max_plane)]

    spack_tracker = {}

    for i in range(d6.max_plane):
        for j in range(d6.max_plane):
            winner = find_closest([i, j])
            space[i][j] = winner
            if winner in spack_tracker:
                spack_tracker[winner] += 1
            else:
                spack_tracker[winner] = 1

    remove = get_outer_edges(space)

    for item in remove:
        del spack_tracker[item]

    print(max(spack_tracker.items(), key=operator.itemgetter(1))[0])
    print(max(spack_tracker.values()))

    # print(space)


def within_10000(coord):

    print(coord)

    safe_zone = 1
    distance_total = 0
    for k, v in d6.coords_dictionary.items():
        distance_total += get_manhatten_closest(coord, v)
        print("{} at {}".format(k, distance_total))
        if distance_total >= 10000:
            return 0

    return safe_zone


def part_two_build_space_and_walk():

    space = [[j for j in range(d6.max_plane)] for i in range(d6.max_plane)]

    safe_total = 0

    coord_list = []

    for i in range(d6.max_plane):
        for j in range(d6.max_plane):
            if within_10000([i, j]):
                safe_total += 1
                coord_list.append([i, j])

    print(safe_total)


if __name__ == '__main__':
    # part_one_build_space_and_walk()

    part_two_build_space_and_walk()
