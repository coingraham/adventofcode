import string

from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=20)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''1
2
-3
3
-2
0
4'''

alternate_sample = '''0
0
1
0
0'''


# Checking if the values are unique, that would let me use list.index as a possibility
# or perhaps track positions in a dictionary
def is_unique(question_input):
    unique = []
    for position, number in enumerate(question_input.splitlines()):

        if number not in unique:
            unique.append(number)
        else:
            print("THEY ARE NOT UNIQUE!!")


# Dictionaries in python are ordered.  So the order I add keys will be retained for looping
# and because they are unique I can easily loop through.
def build_dictionary(question_input, multiplier):
    encrypted_dictionary = {}
    encrypted_list = []

    alphabet = [char for char in string.ascii_lowercase]

    # Loop through the input and save a dictionary and list.
    for position, number in enumerate(question_input.splitlines()):
        number = str(int(number) * multiplier)

        for alpha in alphabet:
            if alpha == "z":
                print("Hold up cowboy, you're going to need to rethink this....")

            new_number = "{}_{}".format(number, alpha)

            if new_number in encrypted_dictionary:
                continue
            else:

                # Add the new number to the list
                encrypted_list.append(new_number)

                # Add the new number to the dictionary.
                encrypted_dictionary[new_number] = False
                break

    return encrypted_list, encrypted_dictionary


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data
    # question_input = alternate_sample

    # is_unique(question_input)

    # Get the encrypted list and dictionary
    e_list, e_dict = build_dictionary(question_input, 1)

    # Get the length once
    e_list_length = len(e_list) - 1

    for item in e_dict.keys():
        # Split the items and set the number
        number, letter = item.split("_")

        # Make an int
        number = int(number)

        # Do nothing on zeros
        if number == 0:
            continue
        # Get the current position of the number
        position = e_list.index(item)

        # Adjust the position by the number itself
        new_pos = position + number

        # Save it to the list.  Note that negative number will just wrap
        # automatically because python just does that.  There is one
        # edge case, if the new position is 0, they want it at the end
        # instead.
        if new_pos == 0:
            e_list.append(e_list.pop(position))
        else:
            if new_pos > e_list_length:
                new_pos = (new_pos % e_list_length)
            elif new_pos == e_list_length:
                new_pos = 0
            elif new_pos < 0:
                new_pos = (new_pos % e_list_length)

            e_list.insert(new_pos, e_list.pop(position))

    # Print the e_list to verify the sample
    print(e_list)

    # Get the 1000, 2000, 3000 after finding the zero
    zero = e_list.index("0_a")

    # Here's the full thing blown out
    get_sum = []
    for x in [1000, 2000, 3000]:
        offset = x + zero
        index_value = offset % (e_list_length + 1)
        number = int(e_list[index_value].split("_")[0])
        get_sum.append(number)

    print(sum(get_sum))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data
    # question_input = alternate_sample

    # is_unique(question_input)

    # Get the encrypted list and dictionary
    e_list, e_dict = build_dictionary(question_input, 811589153)

    # Get the length once
    e_list_length = len(e_list) - 1

    # Part 2:  I need to run through this 10 times
    for cycles in range(10):

        for item in e_dict.keys():
            # Split the items and set the number
            number, letter = item.split("_")

            # Make an int
            number = int(number)

            # Do nothing on zeros
            if number == 0:
                continue
            # Get the current position of the number
            position = e_list.index(item)

            # Adjust the position by the number itself
            new_pos = position + number

            # Save it to the list.  Note that negative number will just wrap
            # automatically because python just does that.  There is one
            # edge case, if the new position is 0, they want it at the end
            # instead.
            # Changing up the logic here to be clearer
            if new_pos < 0 or new_pos >= e_list_length:
                new_pos = (new_pos % e_list_length)

            if new_pos == 0:
                e_list.append(e_list.pop(position))
            else:
                e_list.insert(new_pos, e_list.pop(position))

        # Print the e_list to verify the sample
        # print(e_list)

    # Get the 1000, 2000, 3000 after finding the zero
    zero = e_list.index("0_a")

    # Here's the full thing blown out
    get_sum = []
    for x in [1000, 2000, 3000]:
        offset = x + zero
        index_value = offset % (e_list_length + 1)
        number = int(e_list[index_value].split("_")[0])
        get_sum.append(number)

    print(sum(get_sum))


if __name__ == '__main__':
    # question1()
    question2()

