def d(func):
    print(f"I've registered {func}")
    return func

@d
def bar2():
    print('Bar2')

def bar(): ...
d(bar)
bar2()

def nothing_doing_decorator(func: callable):
    return func
