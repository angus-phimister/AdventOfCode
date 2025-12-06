with open("2025/day6/input.txt") as f:
    input = f.read().split('\n')
    input = [[c for c in x.split(" ") if c !=""] for x in input]

total = 0 
for i in range(len(input[0])):
    if input[-1][i] == "+":
        ind_total=0
        for j in range(3):
            ind_total += int(input[j][i])
    else:
        ind_total=1
        for j in range(3):
            ind_total *= int(input[j][i])    
    
    total += ind_total

print(total) # 17239378288 too low 
breakpoint()
        