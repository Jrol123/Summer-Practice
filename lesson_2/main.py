"""
Второй урок
"""
import math
from collections import defaultdict

lowest_sym = ord('A')

def map(function, nums: list[float]):
    # nums_dub = [0] * len(nums)  # Как НЕ копировать значения, а отсылать в функцию копию?
    return [function(nums[index]) for index in range(len(nums))]


def is_div(num, filt=9):
    return num % filt == 0


def pow_er(num: float, step=2):
    return num ** step


def check_palindrom(word: str) -> bool:
    if len(word) % 2 == 0:
        if word[0:(len(word) // 2)] == word[-1:(len(word) // 2) - 1:-1]:
            return True
        return False

    if word[0:(len(word) // 2)] == word[-1:(len(word) // 2):-1]:
        return True
    return False


def check_prime(num: str) -> bool:
    num = int(num)
    if num <= 1:  # 1 не простое число
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def check_log(num: str, base=2) -> bool:
    return math.log(int(num), base) % 1 == 0


def check_pin(pin_code: list[str]) -> None:
    if check_prime(pin_code[0]) and check_palindrom(pin_code[1]) and check_log(pin_code[2]):
        print("Корректен")
        return
    print("Некорректен")


if __name__ == '__main__':
    case = input()
    match case:
        case 'B':
            values = [1, 3, 1, 5, 7]
            operation = lambda num: num + 5
            print(*map(operation, values))
        case 'C':
            print(sum(map(pow_er, (list(filter(is_div, range(10, 99 + 1)))))))
            # 40905
        case 'D':
            word = input().upper()
            sum_words = {}
            while word:
                sum_words[word] = sum((ord(sym) - lowest_sym + 1) for sym in word)
                word = input().upper()
            print(*dict(sorted(sum_words.items(), key=lambda x: (x[1], x[0]))).keys())

        case 'G':
            check_pin(list(input().split("-")))
            # 7-101-4
            # 12-22-16
