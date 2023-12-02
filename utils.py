from collections import Counter, defaultdict, namedtuple, deque, abc
from dataclasses import dataclass, field
from itertools import permutations, combinations, cycle, chain, islice
from itertools import count as count_from, product as cross_product
from typing import *
from statistics import mean, median
from math import ceil, floor, factorial, gcd, log, log2, log10, sqrt, inf

import matplotlib.pyplot as plt

import ast
import fractions
import functools
import heapq
import operator
import pathlib
import re
import string
import time

current_year = 2022  # Subdirectory name for input files
lines = str.splitlines  # By default, split input text into lines


def paragraphs(text):
    "Split text into paragraphs"
    return text.split("\n\n")


def parse(
    day_or_text: Union[int, str],
    parser: Callable = str,
    sections: Callable = lines,
    show=8,
) -> tuple:
    """Split the input text into `sections`, and apply `parser` to each.
    The first argument is either the text itself, or the day number of a text file."""
    if isinstance(day_or_text, str) and show == 8:
        show = 0  # By default, don't show lines when parsing exampole text.
    start = time.time()
    text = get_text(day_or_text)
    show_items("Puzzle input", text.splitlines(), show)
    records = mapt(parser, sections(text.rstrip()))
    if parser != str or sections != lines:
        show_items("Parsed representation", records, show)
    return records


def get_text(day_or_text: Union[int, str]) -> str:
    """The text used as input to the puzzle: either a string or the day number,
    which denotes the file 'AOC/year/input{day}.txt'."""
    if isinstance(day_or_text, str):
        return day_or_text
    else:
        filename = f"AOC/{current_year}/input{day_or_text}.txt"
        return pathlib.Path(filename).read_text()


def show_items(source, items, show: int, hr="─" * 100):
    """Show the first few items, in a pretty format."""
    if show:
        types = Counter(map(type, items))
        counts = ", ".join(
            f'{n} {t.__name__}{"" if n == 1 else "s"}' for t, n in types.items()
        )
        print(f"{hr}\n{source} ➜ {counts}:\n{hr}")
        for line in items[:show]:
            print(truncate(line))
        if show < len(items):
            print("...")


Char = str  # Intended as the type of a one-character string
Atom = Union[str, float, int]  # The type of a string or number


def ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r"-?[0-9]+", text))


def positive_ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r"[0-9]+", text))


def digits(text: str) -> Tuple[int]:
    """A tuple of all the digits in text (as ints 0–9), ignoring non-digit characters."""
    return mapt(int, re.findall(r"[0-9]", text))


def words(text: str) -> Tuple[str]:
    """A tuple of all the alphabetic words in text, ignoring non-letters."""
    return tuple(re.findall(r"[a-zA-Z]+", text))


def atoms(text: str) -> Tuple[Atom]:
    """A tuple of all the atoms (numbers or identifiers) in text. Skip punctuation."""
    return mapt(atom, re.findall(r"[+-]?\d+\.?\d*|\w+", text))


def atom(text: str) -> Atom:
    """Parse text into a single float or int or str."""
    try:
        x = float(text)
        return round(x) if x.is_integer() else x
    except ValueError:
        return text.strip()


def truncate(object, width=100, ellipsis=" ...") -> str:
    """Use elipsis to truncate `str(object)` to `width` characters, if necessary."""
    string = str(object)
    return (
        string if len(string) <= width else string[: width - len(ellipsis)] + ellipsis
    )


def mapt(function: Callable, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))


def mapl(function: Callable, *sequences) -> list:
    """`map`, with the result as a list."""
    return list(map(function, *sequences))


class multimap(defaultdict):
    """A mapping of {key: [val1, val2, ...]}."""

    def __init__(self, pairs: Iterable[tuple] = (), symmetric=False):
        """Given (key, val) pairs, return {key: [val, ...], ...}.
        If `symmetric` is True, treat (key, val) as (key, val) plus (val, key)."""
        self.default_factory = list
        for key, val in pairs:
            self[key].append(val)
            if symmetric:
                self[val].append(key)


def prod(numbers) -> float:  # Will be math.prod in Python 3.8
    """The product formed by multiplying `numbers` together."""
    result = 1
    for x in numbers:
        result *= x
    return result


def T(matrix: Sequence[Sequence]) -> List[Tuple]:
    """The transpose of a matrix: T([(1,2,3), (4,5,6)]) == [(1,4), (2,5), (3,6)]"""
    return list(zip(*matrix))


def total(counter: Counter) -> int:
    """The sum of all the counts in a Counter."""
    return sum(counter.values())


def minmax(numbers) -> Tuple[int, int]:
    """A tuple of the (minimum, maximum) of numbers."""
    numbers = list(numbers)
    return min(numbers), max(numbers)


def cover(*integers) -> range:
    """A `range` that covers all the given integers, and any in between them.
    cover(lo, hi) is an inclusive (or closed) range, equal to range(lo, hi + 1).
    The same range results from cover(hi, lo) or cover([hi, lo])."""
    if len(integers) == 1:
        integers = the(integers)
    return range(min(integers), max(integers) + 1)


def the(sequence) -> object:
    """Return the one item in a sequence. Raise error if not exactly one."""
    for i, item in enumerate(sequence, 1):
        if i > 1:
            raise ValueError(f"Expected exactly one item in the sequence.")
    return item


def split_at(sequence, i) -> Tuple[Sequence, Sequence]:
    """The sequence split into two pieces: (before position i, and i-and-after)."""
    return sequence[:i], sequence[i:]


def ignore(*args) -> None:
    "Just return None."
    return None


def is_int(x) -> bool:
    "Is x an int?"
    return isinstance(x, int)


def sign(x) -> int:
    "0, +1, or -1"
    return 0 if x == 0 else +1 if x > 0 else -1


def lcm(i, j) -> int:
    "Least common multiple"
    return i * j // gcd(i, j)


def union(sets) -> set:
    "Union of several sets"
    return set().union(*sets)


def intersection(sets):
    "Intersection of several sets; error if no sets."
    first, *rest = sets
    return set(first).intersection(*rest)


def naked_plot(points, marker="o", size=(10, 10), invert=True, square=False, **kwds):
    """Plot `points` without any axis lines or tick marks.
    Optionally specify size, whether square or not, and whether to invery y axis."""
    if size:
        plt.figure(figsize=((size, size) if is_int(size) else size))
    plt.plot(*T(points), marker, **kwds)
    if square:
        plt.axis("square")
    plt.axis("off")
    if invert:
        plt.gca().invert_yaxis()


def clock_mod(i, m) -> int:
    """i % m, but replace a result of 0 with m"""
    # This is like a clock, where 24 mod 12 is 12, not 0.
    return (i % m) or m


def invert_dict(dic) -> dict:
    """Invert a dict, e.g. {1: 'a', 2: 'b'} -> {'a': 1, 'b': 2}."""
    return {dic[x]: x for x in dic}


def walrus(name, value):
    """If you're not in 3.8, and you can't do `x := val`,
    then you can use `walrus('x', val)`."""
    globals()[name] = value
    return value


cat = "".join
cache = functools.lru_cache(None)
Ø = frozenset()  # empty set


def quantify(iterable, pred=bool) -> int:
    """Count the number of items in iterable for which pred is true."""
    return sum(1 for item in iterable if pred(item))


def dotproduct(vec1, vec2):
    """The dot product of two vectors."""
    return sum(map(operator.mul, vec1, vec2))


def powerset(iterable) -> Iterable[tuple]:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return flatten(combinations(s, r) for r in range(len(s) + 1))


flatten = chain.from_iterable  # Yield items from each sequence in turn


def append(sequences) -> Sequence:
    "Append into a list"
    return list(flatten(sequences))


def batched(iterable, n) -> Iterable[tuple]:
    "Batch data into non-overlapping tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    it = iter(iterable)
    while True:
        batch = tuple(islice(it, n))
        if batch:
            yield batch
        else:
            return


def sliding_window(sequence, n) -> Iterable[Sequence]:
    """All length-n subsequences of sequence."""
    return (sequence[i : i + n] for i in range(len(sequence) + 1 - n))


def first(iterable, default=None) -> Optional[object]:
    """The first element in an iterable, or the default if iterable is empty."""
    return next(iter(iterable), default)


def last(iterable) -> Optional[object]:
    """The last element in an iterable."""
    for item in iterable:
        pass
    return item


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def first_true(iterable, default=False):
    """Returns the first true value in the iterable.
    If no true value is found, returns `default`."""
    return next((x for x in iterable if x), default)
