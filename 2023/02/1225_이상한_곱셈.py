import sys

A, B = map(list, sys.stdin.readline().split())
lst_A = list(map(int, A))
lst_B = list(map(int, B))
print(sum(lst_A)*sum(lst_B))