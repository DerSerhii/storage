# Декораторы функций

def decorator(func):
    def wrapper():
        print("--- что-то ПЕРЕД функцией ---")
        func()
        print("--- что-то ПОСЛЕ функции ---")

    return wrapper


# @decorator
def some_func():
    print("Вызов функции some_func")


some_func = decorator(some_func)
some_func()
