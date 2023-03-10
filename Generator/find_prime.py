# Последовательность генераторов
def find_prime(max_num=100):
    num = 1
    while num < max_num:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if num % 2:
            yield num

print(*find_prime(), sep='\t')
print(*find_odd_prime(find_prime()), sep='\t')

