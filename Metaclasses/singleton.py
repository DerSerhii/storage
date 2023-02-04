"""
Класс, который может иметь всего один экземпляр,
"эскиз" для паттерна проектирования Singleton.
"""


# можно было бы реализовать и без метаклассов,
# просто переопределив метод __new__ в базовом классе
class SingletonBase:
    instance = None

    def __new__(cls):
        print(f'{cls.instance= }')

        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class A(SingletonBase):
    pass


class B(A):
    pass


def print_singleton():
    print("*" * 60)
    print("экземпляр класса А: {}".format(A()))
    print("экземпляр класса А: {}".format(A()))
    # B.instance = None
    print("экземпляр класса B: {}".format(B()))


print_singleton()
# при попытке создать экземпляр класса B мы получаем
# в ответ тот же самый экземпляр A, что и раньше.


# решим через метакласс
class SingletonMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.instance = None
        print(f"{'*' * 60}\nInit {cls.__name__} {cls.instance=}")

    def __call__(cls, *args, **kwargs):
        print(f'{cls.instance= }')
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class SingletonBaseMeta(metaclass=SingletonMeta):
    pass


class A(SingletonBaseMeta):
    pass


class B(A):
    pass


print_singleton()

