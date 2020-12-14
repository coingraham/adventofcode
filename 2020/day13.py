import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=13)

example = """939
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"""

start_time, bus_ids = example.split("\n")
# start_time, bus_ids = puzzle.input_data.split("\n")

start_time = int(start_time)
bus_schedule = {int(bus_id): bus_index for bus_index, bus_id in enumerate(bus_ids.split(",")) if bus_id != "x"}
bus_ids_int = [int(item) for item in bus_ids.split(",") if item != "x"]
bus_ids = [item for item in bus_ids.split(",") if item != "x"]

# print(start_time, bus_ids)
# print("time\tbus {}".format("\tbus ".join(bus_ids)))


def search_times(start_time):
    current_time = start_time
    while True:
        report = "{}\t".format(current_time)
        for bus in bus_ids_int:
            if current_time % bus == 0:
                report += "\tD!\t"
                print(report)
                return current_time, bus
            else:
                report += "\t.\t"

        current_time += 1
        print(report)


def find_ordered_times(start, adjustment):
    current_time = start
    saved_results = []
    while True:
        current_time += adjustment
        for bus, position in bus_schedule.items():
            if (current_time + position) % bus != 0:
                break
        else:
            if not saved_results:
                saved_results.append(current_time)
            else:
                saved_results.append(current_time)
                return saved_results


# leave_time, correct_bus = search_times(start_time)
# print("Leaving at {}, on the correct bus {}".format(leave_time, correct_bus))
# print("The product is {}".format((leave_time - start_time) * correct_bus))

found = find_ordered_times(43282261738355, 88924385404026 - 43282261738355)
print(found)


# 779210

