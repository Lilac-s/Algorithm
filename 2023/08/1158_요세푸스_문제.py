from collections import deque
n, k = map(int, input().split(' '))
numbers = deque(list(range(1, n+1)))
result = []
while numbers:
    numbers.rotate(-k+1)
    num = numbers.popleft()
    result.append(num)
print('<', end='')
for i in range(len(result)-1):
    print(f'{result[i]}, ', end='')
print(f'{result[-1]}>')
