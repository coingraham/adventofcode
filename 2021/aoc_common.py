

def print_matrix(matrix):
    return "\n".join([" ".join(item) for item in matrix])


def create_matrix_from_dict(coord_dict, max_size):
    coord_list = list(coord_dict.keys())
    matrix = [["." for j in range(max_size + 1)] for i in range(max_size + 1)]

    for coord in coord_list:
        x, y = [int(n) for n in coord.split(",")]
        matrix[y][x] = "{}".format(coord_dict[coord])

    return matrix
