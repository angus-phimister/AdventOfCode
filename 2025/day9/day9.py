from collections import defaultdict, deque


# with open("2025/day9/test.txt") as f:
#     grid = defaultdict(tuple)
#     for y, row in enumerate(f):
#         for x, char in enumerate(row):
#             grid[(x, y)] = char


# hashes = [key for key, val in grid.items() if val == "#"]

with open("2025/day9/input.txt") as f:
    hashes = [tuple(map(int, x.strip().split(","))) for x in f]

def dist(x:tuple, y:tuple):
    return abs(x[1] - y[1]+1)*abs(x[0] - y[0]+1)


mp = defaultdict(int)

for i,x in enumerate(hashes):
    for k, y in enumerate(hashes):
        if i == k:
            continue
        if (x,y) in mp.keys():
            continue
        mp[(x,y)] = dist(x,y)

max_connection = max(mp, key=mp.get)
print(mp[max_connection])


# Part 2 
# Need to throw out connections where there are not green tiles

breakpoint()