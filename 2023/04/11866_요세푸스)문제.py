from collections import deque

res = list()
n, k = map(int, input().split(" "))
numbers = deque(range(1, n+1))

while numbers:
    for i in range(k-1):
        numbers.append(numbers.popleft())
    res.append(str(numbers.popleft()))

print(f'<{", ".join(res)}>')