from collections import deque
import day23_input as d23
import aoc_updated_intcode as ac


ram = [int(x) for x in d23.input.split(",")]
cq = deque([])
comms = {}
for i in range(50):
    new_ram = ram[::]
    cpu = ac.full_intcode_computer(new_ram.copy(), 0, 0)
    my_in = i
    next(cpu)
    cpu.send([my_in])
    cq.append((i, cpu))
    comms[i] = []


def run_nic(cpu, my_in):
    des = None
    x = None
    y = None
    while True:
        if not my_in:
            my_in = [-1]
        des = cpu.send(my_in)
        if not des:
            return (-1 , [])
        x = next(cpu)
        y = next(cpu)
        return des, [x, y]


# Part One and Two
save = 0
nat_current = None
while True:
    nic = cq.popleft()
    id = nic[0]
    cpu = nic[1]
    if comms[id]:
        my_in = comms[id].pop(0)
    else:
        my_in = []

    if id == 0 and nat_current:
        print("here")

    des, des_out = run_nic(cpu, my_in)
    if des == 255:
        nat_current = des_out
        cq.append((id, cpu))
        continue

    if des != -1:
        comms[des].append(des_out)

    if not any([v for k, v in comms.items()]):
        comms[0].append(nat_current)
        first, last = nat_current
        print(last)
        # if last == save:
        #     print(last)
        #     break
        # else:
        #     save = last

    cq.append((id, cpu))

