import day10_input as d10


def get_adjustment(stars):
    max_x = max(map(lambda x: x[0], stars))
    min_x = min(map(lambda x: x[0], stars))
    max_y = max(map(lambda y: y[1], stars))
    min_y = min(map(lambda y: y[1], stars))

    return min_x, max_x, min_y, max_y


def update_velocity(stars, velocity):
    updated_stars = []
    for i in range(len(stars)):
        try:
            updated_stars.append([stars[i][0] + velocity[i][0], stars[i][1] + velocity[i][1]])
        except:
            print("oops")
    return updated_stars


def check_probable_message(stars):

    score = 0
    length = len(stars)

    for star in stars:
        for item in stars:
            if star == item:
                continue

            if abs(star[0] - item[0]) <= 1 and abs(star[1] - item[1]) <= 1:
                score += 1
                break

    if score/length > .8:
        return True
    else:
        return False


# Just get the max and min and write a printer, don't use arrays
def print_display(stars, velocity):

    counter = 0
    while counter < 50000:
        x0, x1, y0, y1 = get_adjustment(stars)
        if check_probable_message(stars):
            for y in range(y0, y1 + 1):
                print("")
                for x in range(x0, x1 + 1):
                    if [x, y] in stars:
                        print("#", end='')
                    else:
                        print(".", end='')
        counter += 1
        stars = update_velocity(stars, velocity)


if __name__ == '__main__':
    print_display(d10.stars_info, d10.velocity_list)
