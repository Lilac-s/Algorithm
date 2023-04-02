# 다른 사람의 풀이 방법
from sys import stdin
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n, k = map(int, stdin.readline().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))

'''
# 그냥 보이는 대로 푼 방법
n, k = map(int, input().split(" "))
up = 1
for i in range(1, n+1):
    up = up*i

down_front = 1
for i in range(1, k+1):
    down_front = down_front*i

down_back = 1
for i in range(1, n-k+1):
    down_back = down_back*i
print(up//(down_front*down_back))
'''