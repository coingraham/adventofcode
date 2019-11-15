import string
import day5_input


def process_polymer(polymer_list):
    previous_letter = polymer_list[-1]
    skip = False
    remove_items = []
    for i in range(len(polymer_list)-2, -1, -1):
        letter = polymer_list[i]

        if skip:
            skip = False
            previous_letter = letter
            continue

        if letter.isupper() and previous_letter.islower() and previous_letter.upper() == letter:
            remove_items.append(i+1)
            remove_items.append(i)
            skip = True

        if letter.islower() and previous_letter.isupper() and previous_letter.lower() == letter:
            remove_items.append(i+1)
            remove_items.append(i)
            skip = True

        previous_letter = letter

    for remove in remove_items:
        del polymer_list[remove]

    return len(remove_items), polymer_list


if __name__ == '__main__':

    my_polymer_list = list(day5_input.test_polymer)
    my_polymer_original = my_polymer_list.copy()

    finished = True
    while finished:
        finished, my_polymer_list = process_polymer(my_polymer_list)

    print(len(my_polymer_list))

    polymer_length_dict = {}

    for letter in list(string.ascii_lowercase):
        my_polymer_string = day5_input.polymer
        my_polymer_string = my_polymer_string.replace(letter.upper(), '')
        my_polymer_string = my_polymer_string.replace(letter.lower(), '')

        my_polymer_truncated = list(my_polymer_string)

        finished = True
        while finished:
            finished, my_polymer_truncated = process_polymer(my_polymer_truncated)

        polymer_length_dict[letter] = len(my_polymer_truncated)

    # print(polymer_length_dict)
    print(min(polymer_length_dict.values()))



