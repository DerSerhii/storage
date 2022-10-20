a = 188


# ******* OPTION #1 *******
def is_prime(num):
    return True if (all(num % i for i in range(2, num)) and num > 1) else False


print(f"Option #1: {a} -> {is_prime(a)}")


# ******* OPTION #2 *******
def is_prime(num):
    res = True
    d = 2
    while d ** 2 <= num:
        if num % d == 0:
            res = False
            break
        d += 1
    return res


print(f"Option #2: {a} -> {is_prime(a)}")


# ******* OPTION #3 *******
def is_prime(num):
    import math

    # There's only one even prime: 2
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False

    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))

    # We know there's only one even prime, so with that in mind
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in range(3, root + 1, 2):
        if num % i == 0: return False
    return True


print(f"Option #3: {a} -> {is_prime(a)}")

""" ******* FIND OPTION #1 ******* """


def find_prime_factors(number):
    from math import sqrt
    factors, divider = [], 2

    while divider <= int(sqrt(number)):
        if not number % divider:
            factors.append(divider)
            number /= divider
        else:
            divider += 1
    if number > 1:
        factors.append(int(number))
    return factors


print(f"Find option #1: {a} -> {find_prime_factors(a)}")

""" ******* FIND OPTION #2 ******* """


def find_prime_factors(number):
    factors, divisor = [], 2
    while divisor <= number:
        if (number % divisor) == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    return factors


print(f"Find option #2: {a} -> {find_prime_factors(a)}")
