import re
import timeit

with open("2023/Day4/input.txt") as f:
    input = f.readlines()


def make_ints(list):
    return [int(s) for s in list if s != ""]


games = [s.strip("\n").split(":")[1].split("|") for s in input]
games = [[make_ints(s.replace("  ", " ").split(" ")) for s in game] for game in games]

points = 0
for game in games:
    winning_numbers = game[0]
    my_numbers = game[1]

    assert len(set(my_numbers)) == len(my_numbers)

    intersection = list(set(winning_numbers) & set(my_numbers))

    if len(intersection) > 0:
        card_points = 2 ** (len(intersection) - 1)

        points += card_points

print(points)

# Part 2


def part_2():
    cards = {value: 1 for value in range(1, 199)}

    x = 1
    for game in games:
        winning_numbers, my_numbers = [game[0], game[1]]
        card = x
        number_of_repeats = cards[card]

        intersection = list(set(winning_numbers) & set(my_numbers))

        if len(intersection) > 0:
            next_few_cards = [card + i for i in range(1, len(intersection) + 1)]

            for card in next_few_cards:
                cards[card] += number_of_repeats

        x += 1

    total = 0
    for key, value in cards.items():
        total += value

    print(total)


starttime = timeit.default_timer()
print("The start time is :", starttime)
part_2()
print("The time difference is :", timeit.default_timer() - starttime)
