import string


from collections import Counter
import string

from collections import defaultdict


def solveDay(myFile):
    data = parseData(myFile)
    print("Part 1: ", part1(*data, 10))
    print("Part 2: ", part1(*data, 40))


def parseData(myFile):
    myFile = "input"
    polymer, rules = open(myFile).read().split("\n\n")
    polymer = {"".join(pair): 1 for pair in zip(polymer[:-1], polymer[1:])}
    rules = dict(pair.split(" -> ") for pair in rules.splitlines())
    rules = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}
    return polymer, rules


polymer, rules = parseData("input")


def part1(pol, rules, steps):
    for _ in range(steps):
        pol = make_step(pol, rules)
    count = defaultdict(int)
    for k, v in pol.items():
        for ch in k:
            count[ch] += v
    quantities = sorted((item + 1) // 2 for item in count.values())
    return quantities[-1] - quantities[0]


def make_step(polymers, rules):
    new = defaultdict(int)
    for poly, count in polymers.items():
        for rule in rules[poly]:
            new[rule] += count
    return new


solveDay("inupt")

from collections import Counter
import string

lines = [line.strip() for line in open("input.txt", "r").readlines()]
template = lines[0]
rules = [rule.split(" ") for rule in lines[2:]]
rules = {a: (a[0] + c, c + a[1]) for a, b, c in rules}
pairs = ["".join(p) for p in zip(template, template[1:])]

# total the pairs created by substitution
def run(steps):
    ctr = Counter(pairs)
    for i in range(steps):
        newCtr = {key: 0 for key in rules.keys()}
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value
        ctr = newCtr

    letterTotals = {letter: 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letterTotals[key[0]] += value

    # the last character in the template gets another count
    letterTotals[template[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    return lmax - lmin


print("part 1:", run(10))
print("part 2:", run(40))


alphabet = [char for char in string.ascii_uppercase]


with open("pairs.txt") as f:
    maps = f.readlines()

mapping = {
    map.split("->")[0]
    .replace(" ", ""): map.split("->")[1]
    .replace("\n", "")
    .replace(" ", "")
    for map in maps
}


mapping = {}
for map in maps:
    pair = map.split("->")[0].replace(" ", "")
    mapping_letter = map.split("->")[1].replace("\n", "").replace(" ", "")

    mapping_pair1 = f"{pair[0]}{mapping_letter}"
    mapping_pair2 = f"{mapping_letter}{pair[1]}"

    mapping[pair] = {"p1": mapping_pair1, "p2": mapping_pair2}


# Get list of all possible pairs to do the counting
pairs = []
for key, value in mapping.items():

    map1 = value["p1"]
    map2 = value["p2"]

    for pair in [map1, map2, key]:
        if pair not in pairs:
            pairs.append(pair)

values_start = {pair: 0 for pair in pairs}


starting_string = "FNFPPNKPPHSOKFFHOFOC"
# starting_string = "NNCB"

# Starting string to baseline values
for x in range(1, len(starting_string)):
    pair = f"{starting_string[x-1]}{starting_string[x]}"
    # print(pair)
    try:
        values_start[pair] += 1
    except KeyError:
        pass


def add_values(values, mapping):
    values_new = values  # clean slate to add stuff to
    print(f'There are {values["FO"]} FOs')
    for key, value in values.items():

        if value == 0:
            pass
        else:
            # print(key)
            # Find the other pairs this pair maps to
            left_pair = mapping[key]["p1"]
            right_pair = mapping[key]["p2"]

            # Add to the stock of new pairs (by the number of times the existing pair is in original value)
            # print(f'Number of pairs :{values[key]}')
            values_new[left_pair] = values_new[left_pair] + values[key]
            values_new[right_pair] = values_new[right_pair] + values[key]

            # if left_pair == "FO" or right_pair == "FO":
            #     print(f"My key is {key}")
            #     print(f"ive added to FO, its now {values['FO']}")
            #     print(f"There are {values[key]} of my key")

            # if key == "CS":
            #     breakpoint()

    return values_new


value_iterate = values_start
for x in range(0, 10):
    print(f"I'm on iteration {x}")
    value_iterate = add_values(value_iterate, mapping)


# Adding everything together
alphabet = {char: 0 for char in string.ascii_uppercase}
for key, value in value_iterate.items():

    letter1 = key[0]
    letter2 = key[1]

    alphabet[letter1] = alphabet[letter1] + value
    alphabet[letter2] = alphabet[letter2] + value

min_value = 99999
max_value = 0

for letter in string.ascii_uppercase:

    value = alphabet[letter]

    if value < min_value:
        min_value = value

    if value > max_value:
        max_value = value


print(max_value - min_value)

# for key, value in mapping.items():
#     mapping[key] = {'maps':[f"{key[0]}{mapping[key]}",f"{mapping[key]}{key[1]}"], 'value':0}


# # Initializing
# for x in range(1, len(starting_string)):
#     pair = f"{starting_string[x-1]}{starting_string[x]}"
#     print(pair)
#     try:
#         mapping[pair]["value"] += 1
#     except KeyError:
#         pass


# def try_to_add_value(key, map, value):
#     # print('Im trying to add value')
#     try:
#         map[key]["value"] + value
#         return map
#     except KeyError:
#         map[key] = {"value": 1}
#         return map


# def add_polymers_fast(mapping_dict):
#     for key, value in mapping_dict.items():
#         # print(mapping_dict[key]['value'])
#         if mapping_dict[key]["value"] > 0:
#             pairs_to_add = mapping_dict[key]["maps"]
#             print(pairs_to_add)
#             for pair in pairs_to_add:
#                 mapping_dict = try_to_add_value(
#                     pair, mapping_dict, mapping_dict[key]["value"]
#                 )

#     return mapping_dict


# # mapping_new = add_polymers_fast(mapping)


# def add_polymers(starting_string, mapping):
#     ending_string = ""
#     for x in range(1, len(starting_string)):
#         pair = f"{starting_string[x-1]}{starting_string[x]}"

#         if x < len(starting_string) - 1:
#             try:
#                 ending_string = f"{ending_string}{pair[0]}{mapping[pair]}"
#             except KeyError:
#                 ending_string = f"{ending_string}{pair[0]}"
#         else:
#             try:
#                 ending_string = f"{ending_string}{pair[0]}{mapping[pair]}{pair[1]}"
#             except KeyError:
#                 ending_string = f"{ending_string}{pair[0]}{pair[1]}"

#     return ending_string


# # add_polymers(starting_string, mapping)


# for y in range(0, 10):
#     mapping_new = add_polymers_fast(mapping)
#     mapping = mapping_new

# # Counting the letters
# counts = []
# for letter in alphabet:
#     cnt = ending_string.count(letter)
#     if cnt > 0:
#         counts.append(cnt)

# print(max(counts) - min(counts))
