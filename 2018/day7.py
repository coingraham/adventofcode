import day7_input as d7


def map_dependencies():
    dependencies = {}

    for step in d7.step_list:
        instructions_list = step.split(" ")
        letter = instructions_list[7]
        dependency = instructions_list[1]
        if dependency not in dependencies.keys():
            dependencies[dependency] = []
        if letter not in dependencies.keys():
            dependencies[letter] = []

        dependencies[letter].append(dependency)

    print(dependencies)
    return dependencies


def remove_alpha(dependencies, alpha):
    for k, v in dependencies.items():
        if alpha in v:
            dependencies[k].remove(alpha)

    return dependencies


def cycle_through_alphabet():
    dependencies = map_dependencies()
    order = []
    alphabet_list = sorted(dependencies.keys())

    while alphabet_list:
        for alpha in alphabet_list:
            if len(dependencies[alpha]):
                continue
            else:
                order.append(alpha)
                dependencies = remove_alpha(dependencies, alpha)
                alphabet_list.remove(alpha)
                break

    print("".join(order))


def get_work(dependencies, work_done):
    if work_done:
        for alpha in work_done:
            dependencies = remove_alpha(dependencies, alpha)

    order = []
    alphabet_list = sorted(dependencies.keys())

    for alpha in alphabet_list:
        if len(dependencies[alpha]):
            continue
        else:
            order.append(alpha)
            del dependencies[alpha]

    return [dependencies, order]


def log_work(union):
    work_done = []
    for worker in union:
        for k, v in worker.items():
            if v == 1:
                work_done.append(k)
                del worker[k]
                break
            else:
                worker[k] -= 1

    return work_done, union


def assign_work(work_queue, union):
    if not work_queue:
        ongoing = False
        for w in union:
            if w:
                ongoing = True
        return work_queue, union, ongoing
    work_queue = sorted(work_queue)
    for worker in union:
        if not worker and len(work_queue) > 0:
            letter = work_queue.pop(0)
            worker[letter] = d7.alpha_value[letter]

    return work_queue, union, True


def step_through_time():
    time_eplapsed = 0
    dependencies = map_dependencies()
    w1 = {}
    w2 = {}
    w3 = {}
    w4 = {}
    union = [w1, w2, w3, w4]
    work_queue = []
    work_done = []

    work_request = get_work(dependencies, work_done)
    dependencies = work_request[0]
    work_queue.extend(work_request[1])
    work_queue, union, ongoing = assign_work(work_queue, union)

    while ongoing:
        work_done, union = log_work(union)
        work_request = get_work(dependencies, work_done)
        dependencies = work_request[0]
        work_queue.extend(work_request[1])
        work_queue, union, ongoing = assign_work(work_queue, union)
        time_eplapsed += 1

    print(time_eplapsed)


if __name__ == '__main__':
    # cycle_through_alphabet()
    step_through_time()