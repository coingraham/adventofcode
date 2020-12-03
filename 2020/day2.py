example1 = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


with open('day2.in', mode='r') as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def count_valid_passwords(password_list):
    valid = 0
    for item in password_list:
        parts = item.split(" ")
        value_range = parts[0]
        min_max = [int(n) for n in value_range.split("-")]
        letter = parts[1][0]
        password = parts[2]
        password_count = password.count(letter)

        if min_max[0] <= password_count <= min_max[1]:
            valid += 1

    return valid


def check_spaces(password_list):
    valid = 0
    for item in password_list:
        parts = item.split(" ")
        value_range = parts[0]
        min_max = [int(n) - 1 for n in value_range.split("-")]
        letter = parts[1][0]
        password = parts[2]

        if (password[min_max[0]] == letter) is not (password[min_max[1]] == letter):
            valid += 1

    return valid


if __name__ == '__main__':
    # password_list = input.split("\n")

    print(count_valid_passwords(puzzle_input))
    print(check_spaces(puzzle_input))
