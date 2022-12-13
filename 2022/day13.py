from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=13)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''


def evaluate_pairs(packet1, packet2):
    # If the packets are equal, just continue.  I was missing this before, and it
    # was actually a bug that was effecting my code.
    if packet1 == packet2:
        return "continue"

    # If they are two bare numbers, compare and return the result.
    if isinstance(packet1, int) and isinstance(packet2, int):
        if packet1 < packet2:
            return True
        else:
            return False

    # If they are two lists, peal off an item and compare.
    if isinstance(packet1, list) and isinstance(packet2, list):
        max_width = max(len(packet1), len(packet2))

        # Try to load a packet from each list.  If one fails, return the result because
        # it ran out first.
        for counter in range(max_width):
            try:
                left = packet1[counter]
            except:
                return True

            try:
                right = packet2[counter]
            except:
                return False

            # Send the packets back into the function.  This is recursive.
            result = evaluate_pairs(left, right)

            # There are three results possible, if continue I want to keep processing
            # the list, otherwise short circuit (stop processing) and return the result.
            if result == "continue":
                continue
            else:
                return result

    # If there is one int and one list, promote the int to a list and send.
    if isinstance(packet1, int) and isinstance(packet2, list):
        return evaluate_pairs([packet1], packet2)

    # If there is one list and one int, promote the int to a list and send.
    if isinstance(packet1, list) and isinstance(packet2, int):
        return evaluate_pairs(packet1, [packet2])


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    packet_pairs = question_input.split("\n\n")
    good_indexes = []

    # Go through each set of packets and evaluate them
    for number, packet in enumerate(packet_pairs):
        left, right = packet.splitlines()

        # You shouldn't use eval out of very narrow cases.  It works great here.
        packet1 = eval(left)
        packet2 = eval(right)

        # I decided to make a function for this.  It was a good call
        result = evaluate_pairs(packet1, packet2)

        # Collect the results for the puzzle.  The indexes are 1 off.
        if result:
            good_indexes.append(number + 1)

    print(sum(good_indexes))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    split_packets = question_input.splitlines()
    packets = [i for i in split_packets if i]

    sorted_packets = [[[2]], [[6]]]

    for packet in packets:

        left = eval(packet)

        for spot, right in enumerate(sorted_packets):

            if evaluate_pairs(left, right):
                sorted_packets.insert(spot, left)
                break
            else:
                continue

        else:
            sorted_packets.append(left)

    two = sorted_packets.index([[2]]) + 1
    six = sorted_packets.index([[6]]) + 1
    print(two * six)


if __name__ == '__main__':
    question1()
    question2()
