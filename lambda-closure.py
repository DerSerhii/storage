def num():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in num()])
# [6, 6, 6, 6]
"""
<lambda> повертає значення під <i> час виклику.
Викликається <lambda> після завершення циклу, тому <i>=3 до моменту його виклику.

Це через замикання. <i> кешується не в кожен момент часу, 
а як змінна, кінцеве значення якої дорівнює <3>
"""


funcs = [lambda x: x ** i for i in range(2, 4)]
print(funcs[0](5))
# 125
