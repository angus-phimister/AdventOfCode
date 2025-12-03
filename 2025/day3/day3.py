with open("2025/day3/test.txt") as f:
    input = f.readlines()


power_banks = [[int(c) for c in x.strip("\n")] for x in input]

def find_highest_number(list):
    highest = (0,-1)
    for index, num in enumerate(list):
        if num>highest[0]:
            highest = (num,index)
    return highest


# #part 1
# power = []
# for bank in power_banks:
#     first_highest = find_highest_number(bank[:-1]) #index up to 2nd last
#     second_highest = find_highest_number(bank[first_highest[1]+1:]) # from highest onwards
#     total = str(first_highest[0]) + str(second_highest[0])
#     power.append(int(total))

# print(sum(power))

#part 2
power = []
for bank in power_banks:
    len_bank = len(bank)
    total = ""
    highest  = (0,-1)
    for val in range(12):
        index_start = highest[1] + 1
        index_end = -11 + val
        if index_end !=0:
            highest = find_highest_number(bank[index_start:index_end])
        else:
            highest = find_highest_number(bank[index_start:])
        total = total + str(highest[0])
    breakpoint()
    power.append(int(total))

print(sum(power))
breakpoint()