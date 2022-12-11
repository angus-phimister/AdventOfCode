from collections import defaultdict
import string
import itertools as it
import collections
import functools

with open("2022/Day7/input.txt") as f:
    input = [s.rstrip("\n").split(" ") for s in f.readlines()]


def add_element(root, path, data):
    functools.reduce(lambda x, y: x[y], path[:-1], root)[path[-1]] = data


def get_element(root, path):
    return functools.reduce(lambda x, y: x[y], path[:-1], root)[path[-1]]


def tree():
    return collections.defaultdict(tree)


directory_map = tree()


def add_file_size(line: list, current_directory, current_directory_tracker):

    current_value = functools.reduce(
        lambda x, y: x[y], current_directory_tracker, current_directory)['value']

    if current_value is not int:
        current_value = 0

    functools.reduce(lambda x, y: x[y], current_directory_tracker, current_directory)[
        'value'] = current_value + int(line[0])

    return current_directory_tracker, current_directory


def read_command(line: list, directory_map, current_directory_tracker):

    if line[-1] == '..':
        current_directory_tracker.pop()
    else:
        current_directory_tracker.append(line[-1])

    return current_directory_tracker, directory_map


def dir(line: list, directory_map, current_directory_tracker):
    return current_directory_tracker, directory_map


command_map_dict = {"$": read_command, 'dir': dir}

current_directory_tracker = []

for line in input:

    if line[1] == 'ls' or line[1] == 'dir':
        continue
    print(line[1])
    command_type = command_map_dict.get(line[0], add_file_size)

    current_directory_tracker, directory_map = command_type(
        line, directory_map, current_directory_tracker)


def get_size_of_folder(folder):

    agg_size = folder['size']
    for key, value in folder.items():

        if isinstance(value, collections.defaultdict):
            agg_size = agg_size + get_size_of_folder(value)

    return agg_size


def traverse_tree(tree):

    current_total = 0
    # If the tree is a defaultdict, loop over its keys and values

    if isinstance(tree, collections.defaultdict):
        # Im in a folder here
        for key, value in tree.items():
            traverse_tree(value)
    else:
        print(tree)


traverse_tree(directory_map)

# for key, value in directory_map.items():
#     print(key)
#     print(value)

# import modules

# initialise variables
terminal_output = []
filepath = []
sizes = defaultdict(int)
total = 0
max_size = 100000

# read input file
with open('2022/Day7/input.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

# parse input commands
for line in terminal_output:
    # change directories
    if (line.startswith('$ cd')):
        directory = line.split()[-1]
        # go to previous directory
        if (directory == '..'):
            filepath.pop()
        # add directory to filepath
        else:
            filepath.append(directory)

    # list contents
    elif (line.startswith('$ ls')):
        continue

    # parse ls output for sizes
    else:
        size, _ = line.split()
        if (size.isdigit()):
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size

# calculate sum of directories with size at most 100k
for key, value in sizes.items():
    if (value <= 100_000):
        total += value


# print answer
print(total)

# define constants
total_space = 70000000
update_size = 30000000
used_space = sizes['/']
free_space = total_space - used_space
space_needed = update_size - free_space


# find eligible directories to delete
options = []
for key, value in sizes.items():
    if (value > space_needed):
        options.append(value)

# print answer
print(min(options))
