with open("2025/day5/input.txt") as f:
    input = f.read().split('\n')

    i = input.index("")              
    ranges = [[int(c) for c in x.split("-")] for x in input[:i]]
    data = [int(x) for x in input[i+1:]]


def consolidate_ranges(ranges):
    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    return merged

sorted_ranges = consolidate_ranges(ranges)

def check_if_val_in_range(val, r):
    low, high = r[0], r[1]
    return val >= low and val <=high


in_date_ids = []
for value in data:
    for range in sorted_ranges:
        if check_if_val_in_range(value, range):
            in_date_ids.append(value)
            break #skip as we've found it
        
        if value<range[-1]:
            break # sorted ranges, this value only getting bigger

len(in_date_ids)

# Part 2
total = 0
for range in sorted_ranges:
    total += range[1] - range[0] +1
print(total)

# sorted_ranges[0][1] - sorted_ranges[0][0] + 1
breakpoint()