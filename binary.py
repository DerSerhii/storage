"""decimal to binary conversion"""

from selenium import webdriver


def conversion_decimal_to_binary(number: int) -> int:
    lst_bin_num = []
    if number:
        while number > 0:
            lst_bin_num.append(str(number % 2))
            number //= 2
        return int("".join(lst_bin_num)[::-1])
    else:
        return 0


if __name__ == "__main__":
    xx = 1
    print(f'Counted using the built-in function bin(): {bin(xx)[2:]}')
    print(f'Counted using own function: {conversion_decimal_to_binary(xx)}')
