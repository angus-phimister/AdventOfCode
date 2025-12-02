with open("2025/day2/input.txt") as f:
    input = f.readlines()


list_ids = input[0].split(",")
# list_instructions = [s.split(",") for s in input]

def repeated_number(value: int):
    value_str_split = str(value).split()

    numbers_in_string =[]
    for num in value_str_split:
        if num in numbers_in_string:
            return True
        else:
            numbers_in_string.append(num)
    
    return False

def mirror_number(value: int):
    value_str = str(value)
    mid_point = len(value_str)//2

    left = value_str[:mid_point]
    right = value_str[mid_point:]

    if left == right:
        return True
    else:
        return False
    
def repeated_pattern(value: int):
    value_str = str(value)
    return value_str in (value_str + value_str)[1:-1]     


fake_ids = []
for range_ids in list_ids:
    ids = [int(num) for num in range_ids.split("-")]
    for value in range(ids[0], ids[1]+1):
        if repeated_pattern(value):
            fake_ids.append(value)



print(sum(fake_ids))

breakpoint()