"""
Simple decorator
"""
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("--- something before ---")
        func(*args, **kwargs)
        print("--- something after ---", "\n")
    return wrapper


@decorator
def some_func_sugar(*args, **kwargs):
    print(f"Called {some_func_sugar.__name__}")
    print(f"Passed: {args=} {kwargs=}")

some_func_sugar(1, a=1)


def some_func(*args, **kwargs):
    print(f"Called {some_func.__name__}")
    print(f"Passed: {args=} {kwargs=}")

some_func = decorator(some_func)
some_func(100, b=200)
