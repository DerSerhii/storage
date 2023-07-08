"""
Decorator with arguments.
"""
from functools import wraps

def decorator_with_args(arg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("--- something before ---")
            print(f"Passed to decorator: {arg=} ")
            func(*args, **kwargs)
            print("--- something after ---", "\n")
        return wrapper
    return decorator


@decorator_with_args(1)
def some_func_sugar(*args, **kwargs):
    print(f"Called {some_func_sugar.__name__}")
    print(f"Passed: {args=} {kwargs=}")

some_func_sugar(2, a=3)

def some_func(*args, **kwargs):
    print(f"Called {some_func.__name__}")
    print(f"Passed: {args=} {kwargs=}")

some_func = decorator_with_args(100)(some_func)
some_func(200, b=300)
