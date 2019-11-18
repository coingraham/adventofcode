import day8_input as d8


def process_node(input):
    number_of_children = input.pop(0)
    number_of_metadata = input.pop(0)
    score = 0

    for child in range(number_of_children):
        score += process_node(input)

    for meta in range(number_of_metadata):
        score += input.pop(0)

    return score


def process_root_node(input):
    number_of_children = input.pop(0)
    number_of_metadata = input.pop(0)
    score = 0

    child_scores = {}
    for child in range(1, number_of_children + 1):
        child_scores[child] = process_root_node(input)

    if number_of_children == 0:
        for meta in range(number_of_metadata):
            score += input.pop(0)
        return score
    else:
        meta_list = []
        for meta in range(number_of_metadata):
            meta_list.append(input.pop(0))
        for node in meta_list:
            if node in child_scores:
                score += child_scores[node]
        return score


if __name__ == '__main__':

    print(process_node(d8.tree_ints.copy()))

    print(process_root_node(d8.tree_ints.copy()))
