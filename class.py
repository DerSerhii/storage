# import math
#
# class A:
#     A = 20
#     B = 20
#
#     def __init__(self, a, b):
#         A = a
#         B = b
#
#         print(self.A + self.B / 2 + 1)
#
#
# (A(4, 10))
# print(math.factorial(0.6))

# class A:
#     def __init__(self, x, y):
#         self.name = x
#         self.price = y
#
#     def __eq__(self, other):
#         print("Eq")
#         return self.name == other.name and self.price == other.price
#
#
# t1 = A('Audi', 2)
# t2 = A('Audi', 2)
#
# print(t1 == t2)

# class Bike:
#     def __init__(self):
#         self.__Company_name = "BMW"
#         self._price = 2000
#
#     def details(self):
#         print("Name: ", self.__Company_name, "Price: ", self._price)
#
#
# class Car(Bike):
#     def __init__(self):
#         super().__init__()
#         self.__Company_name = "Audi"
#         self._price = 4000
#
#
# obj = Car()
# obj.details()

# class A:
#     num = 0
#
#     def __str__(self):
#         # print(A.num)
#         A.num = A.num + 1
#         # print(A.num)
#         return str(A.num)
#
#
# class B(A):
#     # def __init__(self):
#     #     super().__init__()
#     pass
#
#
# obj = A()
# print('A(): ', obj)
# print('A(): ', obj)
# print('A(): ', obj)
# print('B(): ', B())
#


# class Car:
#     def __init__(self):
#         self.price=2000
#         self.__No_Seats=4
#
#     def details(self):
#         print(self.price)
#         print(self.__No_Seats)
#
#     class a:
#         pass
#
# obj = Car()
# obj.details

# def I(n):
#     s = ""
#     for i in range(n):
#         print("!", end='')
#         s += "*"
#         yield s
#
# a=I(3)
# print(next((a)), end='')
# print(next((a)))
# print(next((a)))
#
# # for x in I(3):
# #     print(x, end='')


# class A:
#     A = 1
#
#     def __init__(self, v=2):
#         self.v = v + A.A
#         A.A += 1
#
#     def set(self, v):
#         print(self.v)
#         self.v += v
#         A.A += 1
#         return
#
# a = A()
# a.set(10)
# print(a.v)
# print(a.__dict__)


# class Student(Exception):
#     def __init__(self, status):
#         print("Failed")
#
# marks = 25
# try:
#     if marks < 33:
#         raise Student("Failed !!")
# except Exception as e:
#     print(e, '+++')

try:
    print(d1/0)
# except:
#     print('Def')
except ZeroDivisionError:
    print('Zero')
except:
    print("except")
else:
    print('else')
