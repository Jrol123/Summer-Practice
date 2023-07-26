"""
A. Весы
"""


class Balance:
    def __init__(self, left_weight: float = 0, right_weight: float = 0):
        self.left = left_weight
        self.right = right_weight

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left > self.right:
            return "L"
        elif self.left < self.right:
            return "R"
        return "="
