def register(func, *args, **kwargs):
    print(f"I've registered {func} with {args=} {kwargs=}")

def deco_register(*args, **kwargs):
    def decorator(func):
        register(func, *args, **kwargs)
        return func
    return decorator


@deco_register(1, a=1)
def foo_1():
    pass

def foo_2():
    pass

register(foo_2, 2, a=2)
