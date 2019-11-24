import math


test1 = 8
test2 = 18
test3 = 42

real = 2694


def get_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    add_serial = power_level + serial
    multiply_by_rid = add_serial * rack_id
    hundreds = (multiply_by_rid // 100) % 10
    return hundreds - 5


def build_fuel_cells(serial):
    plane = [[0 for j in range(0, 300)] for i in range(0, 300)]

    for y in range(0, 300):
        for x in range(0, 300):
            plane[y][x] = get_power(x, y, serial)

    values = 0
    largest_point = []
    # for size in range(1, 301):
    size = 16
    for y in range(0, 301 - size):
        for x in range(0, 301 - size):
            value = 0
            for i in range(size):
                for j in range(size):
                    value += plane[x + i][y + j]
                    if value > values:
                        values = value
                        largest_point = [y, x, size]

    print(largest_point)


if __name__ == '__main__':
    build_fuel_cells(real)
    # [243, 38]
    # 230, 142, 18