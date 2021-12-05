from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=4)

sample_data = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

# question_input = sample_data.split("\n\n")
question_input = puzzle.input_data.split("\n\n")

bingo_list = [n for n in question_input.pop(0).split(",")]


bingo_boards = []

for board_numbers in question_input:
    rows = [n.split() for n in board_numbers.splitlines()]
    total = sum([int(n) for row in rows for n in row])
    rows.extend([[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))])
    bingo_boards.append({"total": total, "consideration": rows, "winner": False})


def part_one_and_two():
    for bingo_called in bingo_list:
        for board in bingo_boards:
            if board["winner"]:
                continue
            found = False
            for options in board["consideration"]:
                try:
                    options.remove(bingo_called)
                except ValueError:
                    continue
                found = True

            if found:
                board["total"] -= int(bingo_called)
                winner = [x for x in board["consideration"] if len(x) == 0]

                if winner:
                    print(board["total"] * int(bingo_called))
                    board["winner"] = True


if __name__ == '__main__':
    part_one_and_two()
