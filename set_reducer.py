"""
Set Reducer
These arrays are too long! Let's reduce them!

Description:
Write a function that takes in an array of integers from 0-9, and returns a new array:

Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
"""


# Example 1
def set_reducer_1(inp: list) -> int:
    while len(inp) != 1:
        n = 1
        res = []
        for i, elem in enumerate(inp):
            try:
                if inp[i] != inp[i + 1]:
                    res.append(n)
                    n = 1
                else:
                    n += 1
            except IndexError:
                if inp[i] != inp[i - 1]:
                    res.append(1)
                else:
                    res.append(n)
        inp = res
    return inp[0]


# Example 2
from itertools import groupby


def set_reducer_2(inp: list) -> int:
    while len(inp) > 1:
        inp = [len(list(group)) for _, group in groupby(inp)]
    return inp[0]


# Example 3
def set_reducer_3(inp: list) -> int:
    return inp[0] if len(inp) == 1 else set_reducer_3([len([*group]) for _, group in groupby(inp)])


##############################################
#                  TEST                      #
##############################################

variables = [
    ([0, 4, 6, 8, 8, 8, 5, 5, 7, 5, 5, 6], 2),
    ([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8], 3),
    ([8, 4, 9, 2, 9, 9, 7, 8, 9, 7, 9, 9, 7, 4, 9, 6, 2, 8, 6, 1, 4,
      4, 0, 2, 1, 3, 9, 3, 2, 4, 9, 2, 2, 5, 3, 3, 1, 6, 4, 2, 5, 1, 2, 3], 2),
]

for var in variables:
    assert set_reducer_1(var[0]) == var[1]
    assert set_reducer_2(var[0]) == var[1]
    assert set_reducer_3(var[0]) == var[1]
    print(f"Tests with variable {var} successful!")
