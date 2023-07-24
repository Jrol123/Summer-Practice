"""
Первый урок.

Были изучены:
+ Базовый синтаксис.
+ Списочные выражения.
+ Срезы.
"""
import math
import sys


def len_points(pt_1: list[float], pt_2: list[float]) -> float:
    """
    Расчёт длин между точками.

    Используется метрика Евклидового пространства

    :param pt_1: 1-я точка
    :type pt_1: list[float]
    :param pt_2: 2-я точка
    :type pt_2: list[float]

    :return: расстояние между ними
    :rtype: float
    """
    return math.sqrt(sum((pt_1[i] - pt_2[i]) ** 2 for i in range(2)))


if __name__ == '__main__':
    num = int(input())
    match num:
        case 1:
            print(sum(1 for i in input() if int(i) % 2 == 0))
        case 2:
            print(min(int(i) for i in input().split()))
        case 3:
            points = [list(map(float, input().split(" "))), list(map(float, input().split(" ")))]
            print(f'{len_points(points[0], points[1]):.3f}')
        case 4:
            count_kegels, count_throws = map(int, input().split())
            kegels = [([i, True])for i in range(count_kegels)]

            for _ in range(count_throws):
                begin_keg, end_keg = map(int, input().split())
                kegs = kegels[begin_keg - 1:end_keg - 1 + 1]
                for keg in kegs:
                    keg[1] = False

            answer = ""
            for keg in kegels:
                if keg[1]:
                    answer += "I"
                else:
                    answer += "."
            print(answer)
        case 5:
            word = input().replace(" ", "").lower()

            if len(word) % 2 == 0:
                if word[0:(len(word) // 2)] == word[-1:(len(word) // 2) - 1:-1]:
                    print("YES")
                    sys.exit(0+1)
                print("NO")
                sys.exit(0+0)

            if word[0:(len(word) // 2)] == word[-1:(len(word) // 2):-1]:
                print("YES")
                sys.exit(2+1)
            print("NO")
            sys.exit(2+0)
        case 6:
            print(" ".join(i for i in input().split() if int(i) % 2 == 0))
