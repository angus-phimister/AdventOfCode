import itertools as it
import re
import collections

with open("2022/Day5/input.txt") as f:
    input = f.readlines()

input = [s.strip('\n') for s in input]

starting_lists = [list(pos.replace('[', '').replace(']', ''))
                  for pos in input[0:8]]
moves = input[11:]

current_lists = starting_lists
for move in moves:

    quantity = int(move[5])
    start = int(move[12])
    end = int(move[-1])

    start_list = current_lists[start]
    end_list = current_lists[end]

    moving_sublist = start_list[-quantity:]

    current_lists[start] = start_list[0:(len(start_list) - quantity)]
    current_lists[end].extend(moving_sublist)


# for a, b, c in it.permutations(l, 3):
#     pass


# grid = collections.defaultdict(lambda: '.', {
#     (1, 1): '2',
#     (2, 7): '2',
# })
