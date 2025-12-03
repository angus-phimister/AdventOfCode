with open("2025/day3/input.txt") as f:
    input = f.readlines()


power_banks = [[int(c) for c in x.strip("\n")] for x in input]

def find_highest_number(list):
    highest = (0,-1)
    for index, num in enumerate(list):
        if num>highest[0]:
            highest = (num,index)
    return highest


#part 1
power = []
for bank in power_banks:
    first_highest = find_highest_number(bank[:-1]) #index up to 2nd last
    second_highest = find_highest_number(bank[first_highest[1]+1:]) # from highest onwards
    total = str(first_highest[0]) + str(second_highest[0])
    power.append(int(total))

# print(sum(power))
def find_highest_number_part2(list, prev_index, val):
    if val !=11:
        sub_list = list[prev_index+1:-11+val]
    else:
        sub_list =list[prev_index+1:]

    highest = (0,-1)
    for index, num in enumerate(sub_list):
        if num>highest[0]:
            highest = (num,index)

    original_index = (prev_index + 1) + highest[1]
    return highest[0], original_index

#part 2
power = []
for bank in power_banks:
    len_bank = len(bank)
    total = ""
    highest_val  = (0,-1)
    for val in range(12):
        prev_index = highest_val[1]
        highest_val = find_highest_number_part2(bank, prev_index, val)
        total = total + str(highest_val[0])
    power.append(int(total))

print(sum(power))
breakpoint()