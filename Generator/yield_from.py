# Обычный yield
import time


def numbers_range_1(n=20):
    for i in range(n):
        yield i

# yield from
def numbers_range_2(n=20):
    yield from range(n)

# yield from – это синтаксический сахар

print(*numbers_range_1(), sep='\t')
print(*numbers_range_2(), sep='\t')



def subgenerator():
    yield 'World'
    time.sleep(1)
    yield 'World'
    time.sleep(1)
    yield 'World'

def generator():
    yield 'Hello'
    time.sleep(1)
    yield from subgenerator()  # Запрашиваем значение из субгенератора
    time.sleep(1)
    yield '!'

for i in generator():
    print(i, end=' ')