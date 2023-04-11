from collections import deque

c = int(input())
for i in range(c):
    numbers = deque(map(int, input().split(" ")))
    n = numbers.popleft()
    aver = sum(numbers)/len(numbers)
    res = 0
    for j in range(n):
        if numbers[j] > aver:
            res += 1
    print('%.3f' %(res/n*100) + '%')
