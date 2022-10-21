class Cities:
    def __init__(self):
        self._cities = ['New York', 'New Delhi', 'Newcastle']

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print("Я __iter__ Городов")
        return CityIterator(self)


class CityIterator:
    def __init__(self, city_obj):
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print("Я __iter__ CityIterator")
        return self

    def __next__(self):
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item


# ************** OUTPUT **************
cities = Cities()
cities_through_iter = CityIterator(cities)

print("Могу работать без __iter__ везде: ", end=" ")
a = CityIterator(cities)
print(next(a), end=".....")
print(next(a), end=".....")
print(next(a))
print()

print("Должен быть __iter__ в итераторе")
for i in cities_through_iter:
    print(i, end=".....")
print("\n")

print("Должен быть __iter__ в итерируемом")
for i in cities:
    print(i, end=".....")
