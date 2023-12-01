with open("2023/Day1/input.txt") as f:
    input = f.readlines()

import re

list_instructions = [s.strip("\n") for s in input]


def get_digits(str1):
    c = []
    for i in str1:
        if i.isdigit():
            c.append(i)

    return int(c[0] + c[-1])


list_digits = [get_digits(string) for string in list_instructions]
print(sum(list_digits))

DIGITS = "1234567890"
DIGITS_AS_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_2_check(s):
    s2 = []
    for i, c in enumerate(s):
        if c in DIGITS:
            s2.append(int(c))
        for word, digit in DIGITS_AS_WORDS.items():
            if s[i:].startswith(word):
                s2.append(digit)
                break
    return s2[0] * 10 + s2[-1]


list_digits_new = [part_2_check(string) for string in list_instructions]
print(sum(list_digits_new))
