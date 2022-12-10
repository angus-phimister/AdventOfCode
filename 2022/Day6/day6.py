import itertools as it
import string

with open("2022/Day6/input.txt") as f:
    input = f.read()

input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

for pos in range(3, len(input)):

    # last_four_letters2 = [input[pos], input[pos-1], input[pos-2], input[pos-3]]
    last_four_letters = [input[idx] for idx in range(pos-3, pos+1)]
    if len(set(last_four_letters)) == 4:
        final_position = pos+1
        break
print(final_position)
