"""
Пример упрощенного ORM

Можно перехватывать параметры, передаваемые конструктору <type>,
изменять их и создавать собственный класс таким образом, как вам угодно.

Единственная вещь, для которой нам нужен наш метакласс – чтобы он
подключался в момент, когда создается наш класс, брал все определения полей
и сохранял их все в одном месте.

Мы будем использовать всего один пакет – для синтаксического разбора/сериализации JSON
"""

import json


class Field:
    """ Базовый класс для всех полей. Каждому полю должно быть присвоено начальное значение """

    def __init__(self, initial_value=None):
        self.initial_value = initial_value

    def validate(self, value):
        """ Проверить, является ли это значение допустимым для данного поля """
        return True


class StringField(Field):
    """ Строковое поле. Опционально в нем можно проверять длину строки """

    def __init__(self, initial_value=None, maximum_length=None):
        super().__init__(initial_value)

        self.maximum_length = maximum_length

    def validate(self, value):
        """ Проверить, является ли это значение допустимым для данного поля """
        if super().validate(value):
            return (value is None) or (isinstance(value, str) and self._validate_length(value))
        else:
            return False

    def _validate_length(self, value):
        """ Проверить, имеет ли строка верную длину """
        return (self.maximum_length is None) or (len(value) <= self.maximum_length)


class IntField(Field):
    """ Целочисленное поле. Опционально можно проверять, является ли записанное в нем число целым"""

    def __init__(self, initial_value=None, maximum_value=None):
        super().__init__(initial_value)

        self.maximum_value = maximum_value

    def validate(self, value):
        """ Проверить, является ли это значение допустимым для данного поля """
        if super().validate(value):
            return (value is None) or (isinstance(value, int) and self._validate_value(value))
        else:
            return False

    def _validate_value(self, value):
        """ Проверить, относится ли целое число к желаемому диапазону """
        return (self.maximum_value is None) or (value <= self.maximum_value)


class ORMMeta(type):
    """ Метакласс для нашего собственного ORM """

    def __new__(mcs, name, bases, namespace):
        fields = {
            name: field
            for name, field in namespace.items()
            if isinstance(field, Field)
        }

        new_namespace = namespace.copy()

        # Удалить поля, относящиеся к переменным класса
        for name in fields.keys():
            del new_namespace[name]

        new_namespace['_fields'] = fields

        return super().__new__(mcs, name, bases, new_namespace)


class ORMBase(metaclass=ORMMeta):
    """ Пользовательский интерфейс для базового класса """

    def __init__(self, json_input=None):
        for name, field in self._fields.items():
            setattr(self, name, field.initial_value)

        # Если предоставляется JSON, то мы разберем его
        if json_input is not None:
            json_value = json.loads(json_input)

            if not isinstance(json_value, dict):
                raise RuntimeError("Supplied JSON must be a dictionary")

            for key, value in json_value.items():
                setattr(self, key, value)

    def __setattr__(self, key, value):
        """ Установщик магического метода """
        if key in self._fields:
            if self._fields[key].validate(value):
                super().__setattr__(key, value)
            else:
                raise AttributeError('Invalid value "{}" for field "{}"'.format(value, key))
        else:
            raise AttributeError('Unknown field "{}"'.format(key))

    def to_json(self):
        """ Преобразовать заданный объект в JSON """
        new_dictionary = {}

        for name in self._fields.keys():
            new_dictionary[name] = getattr(self, name)

        return json.dumps(new_dictionary)


class User(ORMBase):
    """ Пользователь в нашей системе """
    id = IntField(initial_value=0, maximum_value=2**32)
    name = StringField(maximum_length=200)
    surname = StringField(maximum_length=200)
    height = IntField(maximum_value=300)
    year_born = IntField(maximum_value=2017)


a = User('{"name": "serhii"}')
print(a.year_born)
print(a.name)