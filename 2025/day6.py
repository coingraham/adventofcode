from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=6)

sample_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

# question input
q_i = [n for n in sample_data.splitlines()]
# q_i = [n for n in puzzle.input_data.splitlines()]

def part_one():
    answers = 0
    maths = q_i.pop(-1).split()
    maths_len = len(maths)
    questions = [[] for _ in range(maths_len)]
    for q in q_i:
        for i, c in enumerate(q.split()):
            questions[i].append(c)

    for i, q in enumerate(questions):
        if maths[i] == "+":
            answers += sum([int(n) for n in q])
        elif maths[i] == "*":
            product = 1
            for n in q:
                product *= int(n)
            answers += product
    
    return answers

def part_two():
    answers = 0
    maths = q_i.pop(-1).split()
    maths_len = len(maths)
    questions_len = len(q_i[0])

    questions = ["" for _ in range(questions_len)]

    # replace spaces with zeros
    for i, q in enumerate(q_i):
        q_i[i] = q.replace(" ", "0")

    # loop through each question
    for i, q in enumerate(q_i):
        # loop through each character in the question
        for j, c in enumerate(q):
                questions[j] += c
        
    new_questions = [[] for _ in range(maths_len)]
    this_step = 0
    for q in questions:
        if q == '0' * len(q):
            this_step += 1
            continue
        else:
            new = q.strip("0")
            new_questions[this_step].append(new)

    for i, q in enumerate(new_questions):
        if maths[i] == "+":
            answers += sum([int(n) for n in q])
        elif maths[i] == "*":
            product = 1
            for n in q:
                product *= int(n)
            answers += product
    
    return answers

if __name__ == '__main__':
    # print(part_one())
    print(part_two())
