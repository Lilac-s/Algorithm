import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    lst.append((b, a))
lst.sort()
for i in range(n):
    x = lst[i][1]
    y = lst[i][0]
    print(x, y)