class Dispatcher:
    count = 0

    def register_handler(self, func, **kwargs):
        self.count += 1
        report = f'{self.count}. I registered: {func}'
        if kwargs:
            report += f' Passed args: {kwargs}'
        print(report)

    def handler(self, **kwargs):
        def decorator(func):
            self.register_handler(func, **kwargs)
            return func
        return decorator

dp = Dispatcher()

def test():
    print('I will not be printed')

@dp.handler(a=1)
def test2():
    print('I will not be printed')

def test3():
    print('I will not be printed')

test3 = dp.handler(c=1)(test3)

dp.register_handler(test, b=2)
# dp.register_handler(test3)
