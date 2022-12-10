import re
import itertools as it
import string


with open("2022/Day6/input.txt") as f:
    input = [s.rstrip("\n").split(" ") for s in f.readlines()]


def add_file_size(line: list, current_directory):
    print("im adding a file")
    pass


def read_command(line: list, current_directory):
    print("im reading a command")
    pass


def add_directory(line: list, current_directory):
    print("im making sure ive got a directory here")

    pass


command_map_dict = {
    "$": read_command,
    "dir": add_directory,
}

current_directory_map = {"/"}
current_directory_tracker = "/"


for line in input:

    command_type = command_map_dict.get(line[0], add_file_size)
    command_type(line, current_directory_tracker)
