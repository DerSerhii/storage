""" CLOSURE """

from time import perf_counter


# Example 1
def main_func(name):
    def inner_func():
        print("I'm inner function", name)

    return inner_func


# Example 2
def adder(value):
    def inner(a):
        return value + a

    return inner


# Example 3
def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


# Example 4
def average_numbers():
    numbers = []

    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)

    return inner


# Example 5
def average_numbers_im():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa += number
        count += 1
        return summa / count

    return inner


# Example 6
def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


# Example 7
def add(a, b):
    return a + b


def count(func):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"The function '{func.__name__}()' was called {cnt} times")
        return func(*args, **kwargs)

    return inner


