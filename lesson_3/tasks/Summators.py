"""
F. Сумматоры
"""


class Summator:
    list_sum = [1]

    def transform(self, num: int) -> int:
        return num

    def sum(self, end_num):
        if end_num <= len(self.list_sum):
            return self.list_sum[end_num - 1]
        cur_value = self.transform(end_num) + self.sum(end_num - 1)
        self.list_sum.append(cur_value)
        return cur_value


class SquareSummator(Summator):
    list_sum = [1]

    def transform(self, num: int) -> int:
        return num ** 2


class CubeSummator(Summator):
    list_sum = [1]

    def transform(self, num: int) -> int:
        return num ** 3
