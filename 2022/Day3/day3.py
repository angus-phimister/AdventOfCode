import string

priority_order = string.ascii_lowercase + string.ascii_uppercase

with open("2022/Day3/input.txt") as f:
    bags = f.read().split('\n')


def find_common_letter(string1, string2):

    for letter in string1:
        if letter in string2:
            return letter


# Part 1
priority_score = 0
for bag in bags:
    halfway = int(len(bag)/2)
    first_compartment = bag[0:halfway]
    second_compartment = bag[halfway:]

    common_letter = find_common_letter(first_compartment, second_compartment)
    priority_score = priority_score + priority_order.index(common_letter) + 1

print(priority_score)

# Part 2
bags_grouped = [bags[n:n+3] for n in range(0, len(bags), 3)]


def find_common_letter(string_list: list):

    possible_letters = set([item for sublist in [list(string)
                                                 for string in string_list] for item in sublist])
    for letter in possible_letters:
        if all(letter in word for word in string_list):
            return letter


priority_score2 = 0
for group in bags_grouped:
    common_letter = find_common_letter(group)
    priority_score2 = priority_score2 + priority_order.index(common_letter) + 1
print(priority_score2)
