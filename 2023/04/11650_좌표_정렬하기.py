import sys
input = sys.stdin.readline

n = int(input())
lst = list()
for _ in range(n):
    lst.append(list(map(int, input().split(" "))))
lst.sort()
for i in range(n):
    print(" ".join(map(str, lst[i])))