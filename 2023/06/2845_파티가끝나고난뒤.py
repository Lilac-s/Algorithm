import sys
l, p = map(int, sys.stdin.readline().split())
total = l * p
report = list(map(int, sys.stdin.readline().split()))
for i in range(5):
    report[i] -= total
print(*report)