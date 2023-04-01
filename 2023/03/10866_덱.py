from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    order = input().split()
    command = order[0]
    if command == 'push_front':
        num = order[1]
        queue.appendleft(num)
    elif command == 'push_back':
        num = order[1]
        queue.append(num)
    elif command == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)