class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("I'm class decorator")
        result = self.func(*args, **kwargs)
        return result


@MyDecorator
def my_function():
    print("my_function")

my_function()
