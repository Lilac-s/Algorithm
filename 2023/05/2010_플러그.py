import sys
input = sys.stdin.readline

n = int(input())
res = 1
for i in range(n):
    res -= 1
    multitap = int(input())
    res += multitap
print(res)