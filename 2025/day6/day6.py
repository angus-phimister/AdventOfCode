with open("2025/day6/test.txt") as f:
    input = f.read().split('\n')
    input_1 = [[c for c in x.split(" ") if c !=""] for x in input]



# total = 0 
# for i in range(len(input_1[0])):
#     if input_1[-1][i] == "+":
#         ind_total=0
#         for j in range(4):
#             ind_total += int(input_1[j][i])

#     else:
#         ind_total=1
#         for j in range(4):
#             ind_total *= int(input_1[j][i])   

    
#     total += ind_total

# print(total)

# Part 2
nums = input[:3]
operands = [x for x in input[-1].split(" ") if x!=""]


number_sets = []
current_number_set = []
for i in range(len(nums[0])-1,0,-1):
    number = ""
    for j in range(3):
        number+=nums[j][i]
    number = number.replace(" ", "")

    if len(number)>0:
        number = int(number)
        current_number_set.append(number)

    else:
        number_sets.append(current_number_set)
        current_number_set = []


breakpoint()
        