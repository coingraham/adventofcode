from aocd.models import Puzzle
from pprint import pprint
puzzle = Puzzle(year=2022, day=7)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    # pwd is the linux command to print the working directory
    pwd = "/"

    # I'll build a dictionary of the directory structure to gather the files and total sizes
    directory_structure = {
        "/": {
            "total": 0
        }
    }

    for terminal_output in question_input.splitlines():
        # If we cd to root, update the pwd
        if terminal_output == "$ cd /":
            pwd = "/"
            continue

        # We can ignore ls commands
        if terminal_output == "$ ls":
            continue

        # We can ignore dir outputs
        if terminal_output.startswith("dir"):
            continue

        # If we are changing the directory, manage the pwd and create new references
        if terminal_output.startswith("$ cd"):

            # If we go up one level, we just need to remove the last _dir from the pwd
            if terminal_output == "$ cd ..":
                pwd = "_".join(pwd.split("_")[:-1])
                continue

            # If we are going into a directory, get the directory name and update the pwd
            else:
                new_dir = terminal_output.split(" ")[2]
                reference = "{}_{}".format(pwd, new_dir)

                # Edge case where we go into a directory that already exists in our dictionary
                if reference in directory_structure:
                    pwd = reference

                # Otherwise this is the first time we've seen it.  Create the reference and load the total = 0
                else:
                    directory_structure[reference] = {}
                    directory_structure[reference]["total"] = 0
                    pwd = reference

        # Everything else should be output from ls.  Collect that information.
        else:
            # Get the file size and name
            size, name = terminal_output.split(" ")

            # Add the file to the structure, we might need it later
            directory_structure[pwd][name] = size

            # Setup to walk through the parent folders to update the sizes
            directory_list = pwd.split("_")
            working_dir = ""

            # Step through the parent folders and update the size
            for order, dir in enumerate(directory_list):
                # Edge case, the root directory is just "/"
                if order == 0:
                    working_dir += "{}".format(dir)
                    directory_structure[working_dir]["total"] += int(size)

                # The rest add _dir to the end
                else:
                    working_dir += "_{}".format(dir)
                    directory_structure[working_dir]["total"] += int(size)

    # Print during testing and validation
    # pprint(directory_structure)

    total_size = 0
    max_dir_size = 100000

    # Walk through the structure and look for all sizes smaller than max_dir_size
    # add them up and return it
    for k in directory_structure.keys():
        if directory_structure[k]["total"] < max_dir_size:
            total_size += directory_structure[k]["total"]

    print(total_size)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # pwd is the linux command to print the working directory
    pwd = "/"

    # I'll build a dictionary of the directory structure to gather the files and total sizes
    directory_structure = {
        "/": {
            "total": 0
        }
    }

    for terminal_output in question_input.splitlines():
        # If we cd to root, update the pwd
        if terminal_output == "$ cd /":
            pwd = "/"
            continue

        # We can ignore ls commands
        if terminal_output == "$ ls":
            continue

        # We can ignore dir outputs
        if terminal_output.startswith("dir"):
            continue

        # If we are changing the directory, manage the pwd and create new references
        if terminal_output.startswith("$ cd"):

            # If we go up one level, we just need to remove the last _dir from the pwd
            if terminal_output == "$ cd ..":
                pwd = "_".join(pwd.split("_")[:-1])
                continue

            # If we are going into a directory, get the directory name and update the pwd
            else:
                new_dir = terminal_output.split(" ")[2]
                reference = "{}_{}".format(pwd, new_dir)

                # Edge case where we go into a directory that already exists in our dictionary
                if reference in directory_structure:
                    pwd = reference

                # Otherwise this is the first time we've seen it.  Create the reference and load the total = 0
                else:
                    directory_structure[reference] = {}
                    directory_structure[reference]["total"] = 0
                    pwd = reference

        # Everything else should be output from ls.  Collect that information.
        else:
            # Get the file size and name
            size, name = terminal_output.split(" ")

            # Add the file to the structure, we might need it later
            directory_structure[pwd][name] = size

            # Setup to walk through the parent folders to update the sizes
            directory_list = pwd.split("_")
            working_dir = ""

            # Step through the parent folders and update the size
            for order, dir in enumerate(directory_list):
                # Edge case, the root directory is just "/"
                if order == 0:
                    working_dir += "{}".format(dir)
                    directory_structure[working_dir]["total"] += int(size)

                # The rest add _dir to the end
                else:
                    working_dir += "_{}".format(dir)
                    directory_structure[working_dir]["total"] += int(size)

    # Print during testing and validation
    # pprint(directory_structure)

    # Get the space needed to free up
    space_needed = 30000000 - (70000000 - directory_structure["/"]["total"])

    # Build a list of total directory sizes
    directory_space_list = []
    for k in directory_structure.keys():
        directory_space_list.append(directory_structure[k]["total"])

    # Sort the list and step through one at a time until you file the smallest that can be deleted
    for sizes in sorted(directory_space_list):
        if sizes > space_needed:
            print(sizes)
            break


if __name__ == '__main__':
    question1()
    question2()

