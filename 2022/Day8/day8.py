import string
import itertools as it
import functools
import numpy as np

with open('2022/Day8/input.txt') as f:
    input = f.read().split('\n')
    matrix = [[int(x) for x in line] for line in input]

matrix = np.array(matrix)


def above(tree_y, tree_x):
    return matrix[:(tree_y), tree_x]


def bottom(tree_y, tree_x):
    return matrix[(tree_y+1):, tree_x]


def left(tree_y, tree_x):
    return matrix[tree_y, :(tree_x)]


def right(tree_y, tree_x):
    return matrix[tree_y, (tree_x+1):]


direction_start = {
    'top': above,
    'bottom': bottom,
    'left': left,
    'right': right
}


def check_direction(tree):

    tree_y, tree_x = tree[0], tree[1]

    tree_value = matrix[tree_y][tree_x]
    # if tree_x == 1 and tree_y == 3:
    #     breakpoint()

    for key, direction in direction_start.items():
        values_in_way = direction(tree_y, tree_x)
        if tree_value > values_in_way.max():
            print(f'Tree: {tree} is visible from {direction}')
            return True
    return False


def check_view(tree):
    tree_y, tree_x = tree[0], tree[1]

    tree_value = matrix[tree_y][tree_x]

    scienic_score = []
    for key, direction in direction_start.items():
        values_in_way = direction(tree_y, tree_x)

        values_in_way = values_in_way.tolist()
        if key == 'top' or key == 'left':
            values_in_way.reverse()

        number_trees = 0
        for value in values_in_way:
            if tree_value > value:
                number_trees += 1
            elif tree_value <= value:
                number_trees += 1
                break

        print(f"{key} : {number_trees}")

        scienic_score.append(number_trees)

    return np.prod(scienic_score)


# check_direction([1, 1])
# check_direction([1, 3])
# check_direction([2, 1])
# check_direction([2, 2])
# check_direction([3, 2])

check_view([1, 2])


count = 0
scores = []
for x, y in it.product(range(1, matrix.shape[0]-1), range(1, matrix.shape[0]-1)):

    print(matrix)
    print(f"Looking at y:{y}, x:{x} ({matrix[y, x]}) ")
    scores.append(check_view([y, x]))

    # if check_direction([y, x]):
    #     print(matrix)
    #     print(f"I think y:{y}, x:{x} ({matrix[y, x]}) is visible")
    #     count += 1


def count_edges(matrix):

    x, y = matrix.shape

    return 2*x + 2*(y-2)


count = count + count_edges(matrix)
print(count)

print(max(scores))
