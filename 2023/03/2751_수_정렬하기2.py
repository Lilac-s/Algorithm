import sys
input = sys.stdin.readline

numbers = list()
n = int(input())
for i in range(n):
    number = int(input())
    numbers.append(number)

for i in sorted(numbers):
    print(i)