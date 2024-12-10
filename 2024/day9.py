from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=9)

sample_data = 2333133121414131402

# q_i = list(map(int, str(sample_data)))
q_i = list(map(int, str(puzzle.input_data)))


def part_one(q_i):
    disk = []

    # Build disk mapping
    for i, j in enumerate(q_i):
        if i % 2 == 0:
            num = i // 2

            for x in range(j):
                disk.append(num)

        else:
            disk_size = len(disk)
            for y in range(j):
                disk.append(".")

    print(disk)

    # Sort items back to front
    for i, item in enumerate(reversed(disk)):
        space = disk.index(".")

        if isinstance(item, int):
            loc = len(disk) - i - 1
            if loc < space:
                break
            disk[space] = item
            disk[loc] = "."

    # Calculate the checksum
    check_sum = 0
    for i, block in enumerate(disk):
        if block != ".":
            check_sum += i * block

    # print(disk)
    return check_sum


def move_item(disk, item):
    j = len(disk) - 1 - disk[::-1].index(item)
    back_file_item, back_file_len = item

    for i, front_item in enumerate(disk):
        if i == j:
            return disk

        front_file_item, front_file_len = front_item

        if front_file_item != ".":
            continue

        if front_file_len > back_file_len:
            disk[i] = ((front_file_item, front_file_len - back_file_len))
            disk.insert(i, disk.pop(j))
            disk.insert(j + 1, (front_file_item, back_file_len))
            return disk

        elif front_file_len == back_file_len:
            disk[i], disk[j] = disk[j], disk[i]
            return disk


    return disk


def part_two(q_i):
    disk = []

    # Build disk mapping
    for i, j in enumerate(q_i):
        if i % 2 == 0:
            num = i // 2
            disk.append((num, j))

        else:
            if j:
                disk.append((".", j))

    # Sort files back to front
    import copy
    disk_copy = copy.deepcopy(disk)

    for j in range(len(disk_copy) - 1, 0, -1):
        back_file_item, back_file_len = disk_copy[j]

        if back_file_item == ".":
            continue

        disk = move_item(disk, disk_copy[j])


    # Calculate the checksum
    check_sum = 0
    disk_list = []
    for k, v in disk:
        for x in range(v):
            disk_list.append(k)

    for i, block in enumerate(disk_list):
        if block != ".":
            check_sum += i * block

    print(disk_list)
    return check_sum


if __name__ == '__main__':
    print(part_one(q_i))
    print(part_two(q_i))
