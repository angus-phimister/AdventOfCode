import itertools as it
import re
import collections
import string

with open("2022/Day5/input.txt") as f:
    input = [s.rstrip("\n") for s in f.readlines()]

lines = input[0:8]  # 8
formatted = list(zip(*lines))

starting_lists = []
for stack in [1, 5, 9, 13, 17, 21, 25, 29, 33]:
    sublist = list(formatted[stack])
    sublist_format = []
    for letter in sublist:
        if letter in string.ascii_uppercase:
            sublist_format.insert(0, letter)
    starting_lists.append(sublist_format)

# starting_lists = [list(pos.replace("[", "").replace("]", "")) for pos in input[0:8]]
moves = input[10:]  # 10

nmbr = re.sub("[^0-9]", "", moves[0])
current_lists = starting_lists
for move in moves:
    print(f"{move}")

    move_numbers = re.sub("[^0-9]", "", move)

    try:
        quantity = int(move_numbers[:-2])
        start = int(move_numbers[-2])
        end = int(move_numbers[-1])
    except:
        breakpoint()

    print(f"move {quantity} from  {start} to {end} ")

    print(f"Stack {start} is {current_lists[start-1]}")
    print(f"Stack {end} is {current_lists[end-1]}")

    print(current_lists)
    start_list = current_lists[start - 1]
    end_list = current_lists[end - 1]

    moving_sublist = start_list[-quantity:]
    # moving_sublist_format = []
    # for letter in moving_sublist:
    #     moving_sublist_format.insert(-1, letter)

    current_lists[start - 1] = start_list[0 : int(len(start_list) - quantity)]

    current_lists[end - 1].extend(moving_sublist)
    print(current_lists)


answer = []
for ls in current_lists:
    answer.append(ls[-1])

print("".join(answer))
