with open("2025/day1/input.txt") as f:
    input = f.readlines()

list_instructions = [s.strip("\n") for s in input]

positions = [50]
zeros = []

for instruction in list_instructions:
    num_0 = 0
    current_position = positions[-1]
    direction,quantity = instruction[0], int(instruction[1:])
    if direction == "L":
        new_position = current_position - quantity
    elif direction == "R":
        new_position = current_position + quantity

    if new_position == 0:
        num_0 +=1
    else:
        while new_position <0:
            num_0 +=1
            new_position  = 100 + new_position
        
        while new_position >99:
            num_0 +=1
            new_position = new_position - 100

    assert new_position >=0 
    assert new_position <100 

    if (current_position == 0) & (num_0 >0) :
        num_0  = num_0 -1


    positions.append(new_position)
    zeros.append(num_0)
    # print(new_position)


print(sum(zeros))
# print(list_instructions)
# print(positions[1:])
# print(zeros)

total_0 = 0
position = 50
for instruction in list_instructions:
    direction,quantity = instruction[0], int(instruction[1:])

    if direction == "R":
        for _ in range(quantity):
            position +=1
            position %=100
            if position==0:
                total_0 +=1 
    else:
        for _ in range(quantity):
            position -=1
            if position <0:
                position +=100
            if position==0:
                total_0 +=1 
    
print(total_0)


breakpoint()






