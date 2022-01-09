"""     test.assert_equals(prev_mult_of_three(1), None)
        test.assert_equals(prev_mult_of_three(25), None)
        test.assert_equals(prev_mult_of_three(36), 36)
        test.assert_equals(prev_mult_of_three(1244), 12)
        test.assert_equals(prev_mult_of_three(952406), 9)  """

m = 36

# *********** Option N1 ***********
def prev_mult_of_three(n):
    while n % 3:
        n //= 10
    return n or None

print(prev_mult_of_three(m))


# *********** Option N2 ***********
def prev_mult_of_three(n):
    return prev_mult_of_three(n // 10) if n % 3 else n or None

print(prev_mult_of_three(m))


# *********** Option N3 ***********
def prev_mult_of_three(n):
    n_str = str(n)

    while len(n_str):
        if int(n_str) % 3 == 0:
            return int(n_str)
        n_str = n_str[:-1]

print(prev_mult_of_three(m))