"""
Второй урок
"""
import math
import sys
from collections import defaultdict

lowest_sym = ord('A')


def map(function, nums: list[float]):
    # nums_dub = [0] * len(nums)  # Как НЕ копировать значения, а отсылать в функцию копию?
    return [function(nums[index]) for index in range(len(nums))]


def is_div(num: int, filt=9):
    return num % filt == 0


def pow_er(num: float, step=2):
    return num ** step


def check_palindrom(word: str) -> bool:
    return word == word[::-1]


def check_prime(num: str) -> bool:
    num = int(num)
    if num <= 1:  # 1 не простое число
        return False
    for delit in range(2, int(num ** 0.5) + 1):
        if num % delit == 0:
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
    match input():
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
            check_pin(input().split("-"))
            # 7-101-4
            # 12-22-16
        case 'P':
            line = sys.stdin.readline().replace("\n", "")
            words = defaultdict(int)
            while line:
                for word in line.split():
                    words[word] += 1
                line = sys.stdin.readline().replace("\n", "")
            print("\n".join(dict(sorted(words.items(), key=lambda x: (-x[1], x[0]))).keys()))
        case 'Q':
            count_countries = int(input())
            countries = dict()
            # cities, *countr = input().split()
            for _ in range(count_countries):
                cities = list(input().split())  # Можно ли как-то функцией map выделить первый элемент?
                for i in range(1, len(cities)):
                    countries[cities[i]] = cities[0]  # Как упростить?

            for _ in range(int(input())):
                print(countries[input()])
        case 'U':
            # not enough values to unpack (expected 3, got 1)
            people = defaultdict(lambda: defaultdict(int))
            for person, item, count in sys.stdin.readline().split():
                # people[person].append((item, int(count)))  # Добавляет кортеж как набор элементов!
                people[person][item] += int(count)  # Добавляет словарь как набор элементов!
                # .append и += не эквивалентны
            people = dict(sorted(people.items(), key=lambda x: (x[0])))
            for human in people:
                print(human + ":")
                people[human] = dict(sorted(people[human].items(), key=lambda x: (x[0])))
                for purchase in people[human]:
                    print(purchase, people[human][purchase])
    input("Нажмите любую клавишу для продолжения...")
