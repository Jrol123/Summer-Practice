"""
B. Вектор на плоскости
"""

import math


class MyVector:
    def __init__(self, *args: [float | list[float]]):
        """
        Инициализация класса

        :param obj: Список координат вектора в формате (x, y).
        :type obj: tuple[float] | list[float]

        """
        assert all(map(isinstance, args, [(int, float)] * 2))
        if isinstance(args, list):
            self.coords = args
        else:
            self.coords = list(args)

    def x(self):
        return self.coords[0]

    def y(self):
        return self.coords[1]

    def __getitem__(self, item: int):
        return self.coords[item]

    def __add__(self, other):
        return MyVector(*(self[i] + other[i] for i in range(len(self.coords))))

    def __sub__(self, other):
        """
        Разница векторов
        :param other:
        :type other: MyVector

        :return: MyVector

        """
        return MyVector(*(self[i] - other[i] for i in range(len(self.coords))))

    def __mul__(self, other):
        """
        Скалярное произведение
        :param other:
        :return: Float

        """
        if isinstance(other, MyVector):
            return sum([self[i] * other[i] for i in range(0, 1 + 1)])
        elif isinstance(other, float | int):
            return MyVector(*(self[i] * other for i in range(0, 1 + 1)))

    def __imul__(self, other):
        """
        Скалярное произведение
        :param other:
        :return: Float

        """
        if isinstance(other, MyVector):
            return sum([self[i] * other[i] for i in range(0, 1 + 1)])
        elif isinstance(other, float | int):
            self.coords = list(self[i] * other for i in range(0, 1 + 1))
            return self

    def __rmul__(self, other):
        assert isinstance(other, (int, float))
        return self * other

    def __pow__(self, vc):
        """
        Векторное произведение
        :param vc:
        :type vc: MyVector
        :return: Вектор, являющийся результатом векторного произведения двух векторов
        """
        return MyVector(self[1] * vc[2] - self[2] * vc[1], - (self[0] * vc[2] - self[2] * vc[0]),
                        self[0] * vc[1] - self[1] * vc[0])  # Не сократить из-за особой формулы

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not self.__eq__(other)

    def __abs__(self) -> float:
        """
        Вычисление длины вектора.

        :return: Длина вектора.
        :rtype: float

        """
        return math.sqrt(self[0] ** 2 - self[1] ** 2)

    def __str__(self) -> str:
        return f"MyVector({self[0]}, {self[1]})"
