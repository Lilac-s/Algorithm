import sys

N = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(N)]
stick = stack.pop()
cnt = 1

for i in range(1, N):
    height = stack.pop()

    if height > stick:
        cnt += 1
        stick = height

print(cnt)