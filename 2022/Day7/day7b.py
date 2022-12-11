# import modules
from collections import defaultdict

# initialise lists
terminal_output = []
filepath = []
sizes = defaultdict(int)

# define constants
total_space = 70000000
update_size = 30000000
used_space = sizes['/']
free_space = total_space - used_space
space_needed = update_size - free_space

# read input file
with open('2022/Day7/input.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

# parse terminal output
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

# find eligible directories to delete
options = []
for key, value in sizes.items():
    if (value > space_needed):
        options.append(value)

# print answer
print(min(options))
