from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=2)

sample_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

# sample_data = """L150"""

# question input
# q_i = [n for n in sample_data.split(",")]
q_i = [n for n in puzzle.input_data.split(",")]

safe_options = [n for n in range(100)]

def part_one():
    # Brute force
    naughty_list = []

    for number_range in q_i:
        start, end = number_range.split("-")
        for number in range(int(start), int(end)+1):
            s = str(number)
            length = len(s)
            if length %  2 == 1:
                continue
            else:
                mid = length // 2
                if s[:mid] == s[mid:]:
                    print(f"Found {number}")
                    naughty_list.append(number)

    return sum(naughty_list)
                

def part_two():
    big_repeat_number_list = []

    for number in range(1, 10):
        for length in range(2, 15):
            big_repeat_number_list.append(int(str(number) * length))

    for number in range(10, 100):
        for length in range(2, 7):
            big_repeat_number_list.append(int(str(number) * length))

    for number in range(100, 1000):
        for length in range(2, 4):
            big_repeat_number_list.append(int(str(number) * length))

    for number in range(1000, 10000):
        for length in range(2, 3):
            big_repeat_number_list.append(int(str(number) * length))

        naughty_list = []

    for number_range in q_i:
        start, end = number_range.split("-")
        for number in range(int(start), int(end)+1):
            if number in big_repeat_number_list:
                naughty_list.append(number)
                continue
            s = str(number)
            length = len(s)
            if length %  2 == 1:
                continue
            else:
                mid = length // 2
                if s[:mid] == s[mid:]:
                    print(f"Found {number}")
                    naughty_list.append(number)

    return sum(naughty_list)


if __name__ == '__main__':
    # print(part_one())
    print(part_two())
