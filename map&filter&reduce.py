# MAP(func, *iterables)

word = ['table', 'chair', 'pen']

# without MAP
word_upper = []
for w in word:
    word_upper.append(w.upper())
print(word_upper)

# with MAP
word_upper = list(map(str.upper, word))
print(word_upper)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.0001379679]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings, my_numbers))
print(results)

# my zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x, y: (x + y), a, b)))
print(list(map(lambda x: x - 10, a)))

# FILTER(func, iterable)

scores = sorted([66, 90, 68, 59, 76, 60, 88, 74, 81, 65])
print(list(filter(lambda x: x > 70, scores)))

# REDUSE(func, iterable[, initial])
from functools import reduce

numbers = [5, 5, 5, 5]


result1 = reduce(lambda x, y: x + y, numbers)
result2 = reduce(lambda x, y: x + y, numbers[1:])
result3 = reduce(lambda x, y: x + y, numbers, 100)
print(sum(numbers), result1, result2, result3)
