with open("2022/Day2/input.txt") as f:
    input = f.readlines()

list_games = [s.strip('\n') for s in input]


def base_points(shape):
    if shape == 'R':
        return 1
    if shape == 'P':
        return 2
    if shape == 'S':
        return 3


def convert_shape(shape, mine=True):
    if mine:
        if shape == 'X':
            return 'R'
        if shape == 'Y':
            return 'P'
        if shape == 'Z':
            return 'S'
    else:
        if shape == 'A':
            return 'R'
        if shape == 'B':
            return 'P'
        if shape == 'C':
            return 'S'


def game_result(my_shape, oppoonent_shape):

    if my_shape == 'R' and oppoonent_shape == 'S':
        return 6
    if my_shape == 'R' and oppoonent_shape == 'P':
        return 0
    if my_shape == 'R' and oppoonent_shape == 'R':
        return 3

    if my_shape == 'P' and oppoonent_shape == 'S':
        return 0
    if my_shape == 'P' and oppoonent_shape == 'P':
        return 3
    if my_shape == 'P' and oppoonent_shape == 'R':
        return 6

    if my_shape == 'S' and oppoonent_shape == 'S':
        return 3
    if my_shape == 'S' and oppoonent_shape == 'P':
        return 6
    if my_shape == 'S' and oppoonent_shape == 'R':
        return 0


points = 0
for game in list_games:

    my_shape = convert_shape(game[-1])
    opp_shape = convert_shape(game[0], mine=False)

    result = game_result(my_shape, opp_shape)
    base = base_points(my_shape)
    points = points + result + base


def choose_shape(opp_shape, result_required):

    if result_required == 'X' and opp_shape == 'R':
        return 'S'
    if result_required == 'Y' and opp_shape == 'R':
        return 'R'
    if result_required == 'Z' and opp_shape == 'R':
        return 'P'

    if result_required == 'X' and opp_shape == 'P':
        return 'R'
    if result_required == 'Y' and opp_shape == 'P':
        return 'P'
    if result_required == 'Z' and opp_shape == 'P':
        return 'S'

    if result_required == 'X' and opp_shape == 'S':
        return 'P'
    if result_required == 'Y' and opp_shape == 'S':
        return 'S'
    if result_required == 'Z' and opp_shape == 'S':
        return 'R'


points_part2 = 0
for game in list_games:

    opp_shape = convert_shape(game[0], mine=False)
    my_shape = choose_shape(opp_shape, game[-1])

    result = game_result(my_shape, opp_shape)
    base = base_points(my_shape)
    points_part2 = points_part2 + result + base
