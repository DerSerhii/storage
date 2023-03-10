def calc():
    history = []
    while True:
        x = yield
        if x == 'h':
            print(history)
            continue
        print(x)
        history.append(x)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send(1)  # Выведет 1
c.send(100)  # Выведет 100
c.send(666)  # Выведет 666
c.send('h')  # Выведет [1, 100, 666]
c.close()  # Закрываем генератор, данные сотрутся, генератор необходимо будет создавать заново.


# Пример с передачей более чем одного параметра
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send((1, 2))  # Выведет 3
c.send((100, 30))  # Выведет 130
c.send((666, 0))  # Выведет 666
c.send(('h', 0))  # Выведет [3, 130, 666]
c.close()  # Закрывем генератор, данные сотрутся, генератор необходимо будет создавать заново.


# Корутин как декоратор
def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen

    return wrap


@coroutine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)

c = calc()

# next(c)  инициация не нужна
c.send((4, 5))
c.send((34, 34))
c.send((63, 0))
c.send(('h', 0))
c.close()  # Закрывем генератор, данные сотрутся, генератор необходимо будет создавать заново.
