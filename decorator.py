# Декораторы функций

def decorator(func):
    def wrapper():
        print("--- что-то ПЕРЕД функцией ---")
        func()
        print("--- что-то ПОСЛЕ функции ---")
    
    return wrapper  # возвращаем объект типа <class 'function'>


# @decorator
def some_func():
    print("Вызов функции some_func")


some_func = decorator(some_func)
some_func()

# --- что-то ПЕРЕД функцией ---
# Вызов функции some_func
# --- что-то ПОСЛЕ функции ---


# def my_decorator(func):
#     print("Я обычная функция")
#     def wrapper():
#         print("Я - функция, возвращаемая декоратором")
#         func()
#     return wrapper
#
# def lazy_function():
#     print("zzzzzzzz")
#
# decorated_function = my_decorator(lazy_function)
#
# # @my_decorator
# # def lazy_function():
# #     print("zzzzzzzz")

