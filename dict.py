""" Dictionary operations """

d1 = {1: "a", 2: "b", 3: "c"}

# Поменять местами значения с ключами
dd1 = {i: j for j, i in d1.items()}
print(d1, dd1, sep="....")

# Отсортировать данне словаря
d2 = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
print(*sorted(d2.items(), key=lambda x: int(x[0])))
print(*sorted(d2.values(), key=lambda x: int(x)))
print(*sorted(d2.keys(), key=lambda x: int(x)))

print({k: v for k, v in sorted(d2.items(), key=lambda x: (int(x[0][1:]), x[1]))})
