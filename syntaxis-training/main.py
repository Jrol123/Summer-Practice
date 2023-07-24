"""
Main test substance
"""

if __name__ == '__main__':
    state = bool(int(input()))
    if not state:
        # 123456
        # 13579

        print(sum(1 for i in input() if int(i) % 2 == 0))
    else:
        print(min(int(i) for i in input().split()))
