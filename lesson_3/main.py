"""
Третья лекция.

Посвящена ООП.

Зона тестирования.
"""

from tasks.Balance import *
from tasks.MyVector import *
from tasks.Queue import *
from tasks.Spam import *
from tasks.Summators import *

def a_test1():
    balance = Balance(0, 0)
    balance.add_right(10)
    balance.add_left(9)
    balance.add_left(2)
    print(balance.result())


def a_test2():
    balance = Balance(0, 0)
    balance.add_right(10)
    balance.add_left(5)
    balance.add_left(5)
    print(balance.result())
    balance.add_left(1)
    print(balance.result())


def b_test1():
    """Проверка на сложение."""
    v1 = MyVector(-2, 5)
    v2 = MyVector(3, -4)
    v_sum = v1 + v2
    v_div = v1 - v2
    print(v_sum)
    print(v_div)


def b_test2():
    """Проверка на умножение."""
    v1 = MyVector(-2, 5)
    print(v1 * 5)
    print(5 * v1)
    print(v1)
    v1 *= -1
    print(v1)


def d_test1():
    book1 = {}
    artem = Person("Artem", "Popovkin", "Andreevich", book1)
    print(artem.get_name())
    print(artem.get_phone())
    print(artem.get_work_phone())
    print(artem.get_sms_text())

    # book3 = {"private": ["11", "22"]}
    print()

    book2 = {"private": "8800", "work": "5553535"}
    oleg = Person("Oleg", "Olegovon", "Olegovich", book2)
    print(oleg.get_name())
    print(oleg.get_phone())
    print(oleg.get_work_phone())
    print(oleg.get_sms_text())

    print()

    company = Company("Foundation", "science", dict(), artem, oleg)
    print(company.get_name())
    print(company.get_phone())
    print(company.get_sms_text())

    send_sms(company, artem, oleg)


def d_test2():
    person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
    person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
    person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
    person4 = Person("John", "Unknown", "Doe", {})

    company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
    company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
    company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)

    send_sms(person1, person2, person3, person4, company1, company2, company3)


def e_test2():
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    qx = q1.copy()
    print(qx.pop())
    print(qx)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q2.next()
    print(q1, q2, q3, sep='\n')
    print(q1 + q3)
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4)  # ?
    print(q4)
    print(q5)


def e_test1():
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    print(q1.pop())
    print(q1)


def f_test1():
    # Абстрактный класс.

    # ! Будет перезаписан лист общий для класса,
    # поэтому при создании summator1 = Summator() он уже будет иметь изменённый лист!
    print(Summator().sum(5))  # 15
    print(Summator().sum(4))  # 10
    print(Summator().sum(7))  # 28

    print()

    print(SquareSummator().sum(5))  # 55
    print(SquareSummator().sum(4))  # 30
    print(SquareSummator().sum(7))  # 140

    print()

    print(CubeSummator().sum(5))  # 225
    print(CubeSummator().sum(4))  # 100
    print(CubeSummator().sum(7))  # 184


if __name__ == '__main__':
    match (input()):
        case 'A':
            match (int(input())):
                case 1:
                    a_test1()
                case 2:
                    a_test2()
        case 'B':
            match (int(input())):
                case 1:
                    b_test1()
                case 2:
                    b_test2()
        case 'D':
            match (int(input())):
                case 1:
                    d_test1()
                case 2:
                    d_test2()
        case 'E':
            match (int(input())):
                case 1:
                    e_test2()
                case 2:
                    e_test1()
        case 'F':
            match (int(input())):
                case 1:
                    f_test1()
