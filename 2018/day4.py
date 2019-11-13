import day4_input as d4
import operator
from datetime import timedelta


def part_one(entries):

    # Tracking variables
    current_guard_id = 0
    current_sleep_time = None

    # Most sleepy guard
    guard_sleep_time_log = {}

    # Guard sleep minute count
    guard_sleep_minute_count = {}

    for entry in entries:
        time_entry = entry[0]
        log_entry = entry[1]
        if log_entry.startswith("Guard"):
            current_guard_id = log_entry.split(" ")[1].lstrip("#")
        elif log_entry.startswith("falls"):
            current_sleep_time = time_entry
        else:
            time_slept = current_sleep_time - time_entry
            minutes_asleep = abs(time_slept / timedelta(minutes=1))

            # Most sleepy guard logic
            if current_guard_id in guard_sleep_time_log:
                guard_sleep_time_log[current_guard_id] += minutes_asleep
            else:
                guard_sleep_time_log[current_guard_id] = minutes_asleep

            # Guard sleep minute count logic
            sleep_start_minute = int(current_sleep_time.minute)
            sleep_stop_minute = int(time_entry.minute)
            for minute in range(sleep_start_minute, sleep_stop_minute):
                minute_key = "{}_{}".format(current_guard_id, minute)
                if minute_key in guard_sleep_minute_count:
                    guard_sleep_minute_count[minute_key] += 1
                else:
                    guard_sleep_minute_count[minute_key] = 1

    most_sleepy_guard = max(guard_sleep_time_log.items(), key=operator.itemgetter(1))[0]
    print("Most Sleepy Guard is: {}".format(most_sleepy_guard))

    filtered_guard_sleep_minute = {k: v for k, v in guard_sleep_minute_count.items() if k.startswith(most_sleepy_guard)}
    most_sleepy_minute = max(filtered_guard_sleep_minute.items(), key=operator.itemgetter(1))[0]
    print("Most Sleepy Minute is: {}".format(most_sleepy_minute))

    multiplied_answer = int(most_sleepy_minute.split("_")[0]) * int(most_sleepy_minute.split("_")[1])
    print("Multiplied: {}".format(multiplied_answer))

    most_sleepy_minute_all_guards = max(guard_sleep_minute_count.items(), key=operator.itemgetter(1))[0]
    print("Most Sleepy Minute For All is: {}".format(most_sleepy_minute_all_guards))

    multiplied_answer = int(most_sleepy_minute_all_guards.split("_")[0]) * int(most_sleepy_minute_all_guards.split("_")[1])
    print("Multiplied: {}".format(multiplied_answer))

if __name__ == '__main__':
    sorted_logs = d4.sorted_entries

    part_one(sorted_logs)