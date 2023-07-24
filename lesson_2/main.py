"""
Второй урок
"""


def map(function, nums: list[float]):
    for index in range(len(nums)):
        nums[index] = function(nums[index])


if __name__ == '__main__':
    values = [1, 3, 1, 5, 7]
    operation = lambda x: x + 5
    map(operation, values)
    print(*values)
