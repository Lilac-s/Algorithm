import sys
from collections import deque
'''
시간 초과가 발생한 코드 - 재귀 사용
def travel(x, y, cnt):
    global res, maze
    if cnt >= res-1:
        return
    if x == n-1 and y == m-1:
        res = min(res, cnt)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = 0
            travel(nx, ny, cnt+1)
            maze[nx][ny] = 1
    return
'''

# BFS
def travel():
    global maze
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                queue.append((nx, ny, cnt+1))

n, m = map(int, sys.stdin.readline().strip().split(' '))
maze = list(list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = travel()
print(res)
