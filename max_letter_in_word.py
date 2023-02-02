"""
Посчитать максимальное количество одинаковых букв без учета регистра
"""

from itertools import groupby


def get_max_letter_1(word: str) -> int:
    word_list_sort = sorted(list(word.lower()))
    # return max({len(list(group)) for _, group in groupby(word_list_sort)})
    # list(group) <=> [*group]
    return max({len([*group]) for _, group in groupby(word_list_sort)})


def get_max_letter_2(word: str) -> int:
    word_list = list(word.lower())
    letter_uniq = set(word_list)
    letter_dict = dict.fromkeys(letter_uniq, 0)

    for i in word_list:
        letter_dict[i] += 1

    return max(letter_dict.values())


##############################################
#                  TEST                      #
##############################################

variables = [
    ("Awbtbra", 2),
    ("AaA", 3)

]

for var in variables:
    assert get_max_letter_1(var[0]) == var[1]
    assert get_max_letter_2(var[0]) == var[1]
    print(f"Tests with variable {var} successful!")
