with open("2022/Day1/input.txt") as f:
    input = f.readlines()

list_calories = [s.strip('\n') for s in input]

list_of_lists = []
sublist = []
for item in list_calories:
    if item != "":
        sublist.append(int(item))
    else:
        list_of_lists.append(sublist)
        sublist = []
if sublist != []:
    list_of_lists.append(sublist)

# Part 1
max_value = 0
for lst in list_of_lists:
    value = sum(lst)

    if value > max_value:
        max_value = value
print(max_value)

# Part 2
value_list = [sum(lst) for lst in list_of_lists]
max_three = sum(sorted(value_list)[-3:])
