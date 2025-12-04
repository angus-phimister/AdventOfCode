with open("2025/day4/input.txt") as f:
    input = f.readlines()


grid = [[c for c in x.strip("\n")] for x in input]

HEIGHT = len(grid)
WIDTH = len(grid[0])


adjacent_offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def get_adjacent_positions(x, y, grid_width=WIDTH, grid_height=HEIGHT):
    adjacent = []
    for dx, dy in adjacent_offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            adjacent.append((nx, ny)) 
    return adjacent

def count_around(x,y):
    adjacent_positions = get_adjacent_positions(x,y)
    count = 0
    for position in adjacent_positions:
        val = grid[position[1]][position[0]]
        if val == "@":
            count +=1
    return count


# Part 1 
total=0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == ".":
            continue
        adj_count = count_around(x,y)

        if adj_count<4:
            total += 1


# Part 2

def make_new_grid(grid, index_to_replace:list):
    grid_new = grid
    for index in index_to_replace:
        grid_new[index[1]][index[0]]  = "."
    return grid_new

def round_of_clearing(grid):
    total_removed=0
    index_to_replace = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == ".":
                continue
            adj_count = count_around(x,y)

            if adj_count<4:
                total_removed += 1
                index_to_replace.append((x,y))

    new_grid = make_new_grid(grid, index_to_replace)
    return new_grid, total_removed

removed_this_round=1
overall_total = 0
while removed_this_round>0:
    grid, removed_this_round = round_of_clearing(grid)
    overall_total += removed_this_round


print(overall_total)
breakpoint()
