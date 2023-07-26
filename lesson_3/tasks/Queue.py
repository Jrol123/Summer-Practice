"""
E. Очередь
"""


class Queue:
    def __init__(self, *values: list[int | float | str] | int | float | str):
        if len(values) == 0:
            raise ValueError("Количество элементов = 0")
        if isinstance(values[0], list):
            self.q = values[0]
        else:
            self.q = list(values)

    def append(self, *values: int | float | str):
        if len(values) == 0:
            raise ValueError("Количество элементов = 0")
        self.q.extend(values)

    def copy(self):
        return Queue(self.q.copy())

    def pop(self) -> int | float | str | None:
        try:
            value = self.q[0]
            rem_first(self.q)
            return value
        except:
            return None

    def extend(self, other: "Queue"):
        self.q.extend(other.q)

    def next(self):
        try:
            a = self.q.copy()
            rem_first(a)
            return Queue(a)
        except:
            return None

    def __add__(self, other):
        a = self.q.copy()
        a.extend(other.q)
        return Queue(a)

    def __iadd__(self, other):
        # Фактически extend и += выполняют одинаковые функции
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.q == other.q

    def __rshift__(self, other):
        a = self.q.copy()
        for _ in range(other):
            rem_first(a)
        return Queue(a)

    def __str__(self) -> str:
        return "[" + "->".join(str(element) for element in self.q) + "]"


def rem_first(a: list):
    a.remove(a[0])


def next(other: "Queue"):
    try:
        a = other.q.copy()
        rem_first(a)
        return Queue(a)
    except:
        return None
