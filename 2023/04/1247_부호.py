import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    res = 0
    for _ in range(n):
        num = int(input())
        res += num
    if res == 0:
        print('0')
    elif res > 0:
        print('+')
    elif res < 0:
        print('-')