import sys
N = int(input())
lst = [0]*10001
for i in range(N):
    number = int(sys.stdin.readline())
    lst[number] += 1

for j in range(len(lst)):
    if lst[j] != 0:
        for k in range(lst[j]):
            print(j)
