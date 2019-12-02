import numpy


if __name__ == '__main__':

    test1 = 8
    test2 = 18
    test3 = 42
    real = 2694

    serial = int(real)

    def get_power(x, y):
        rack_id = (x + 1) + 10
        power_level = rack_id * (y + 1)
        add_serial = power_level + serial
        multiply_by_rid = add_serial * rack_id
        hundreds = (multiply_by_rid // 100 % 10) - 5
        return hundreds


    grid = numpy.fromfunction(get_power, (300, 300))

    integral = grid.cumsum(axis=0).cumsum(axis=1)
    integral = integral.astype(int)


    # This is the calculation of the summed area table: https://en.wikipedia.org/wiki/Summed-area_table
    def check_window(x, y, width):
        offset = width - 1
        x_offset = x + offset
        y_offset = y + offset
        total = integral[x_offset][y_offset]
        top = integral[x_offset][y - 1] if y > 0 else 0
        left = integral[x - 1][y_offset] if x > 0 else 0
        overlap = integral[x - 1][y - 1] if x > 0 and y > 0 else 0
        return total - top - left + overlap


    for width in range(3, 300):
        # windows = numpy.fromfunction(check_window, (300 - width + 1, 300 - width + 1), int, width=width) # can't figure out how to make this work
        windows = numpy.zeros((300 - width + 1, 300 - width + 1), int)
        for i in range(300 - width + 1):
            for j in range(300 - width + 1):
                windows[i][j] = check_window(i, j, width)
        maximum = int(windows.max())
        location = numpy.where(windows == maximum)
        print(width, maximum, location[0][0] + 1, location[1][0] + 1)
