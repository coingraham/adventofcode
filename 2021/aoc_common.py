

def print_matrix(matrix):
    return "\n".join([" ".join(item) for item in matrix])


def create_matrix(coord_dict):
    coord_list = list(coord_dict.keys())
    matrix = [["." for j in range(10)] for i in range(10)]

    for coord in coord_list:
        x, y = [int(n) for n in coord.split(",")]
        matrix[y][x] = "{}".format(coord_dict[coord])

    return matrix
