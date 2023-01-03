import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 1, -1,  1, -1, 0, 0]
dy = [1, -1, -1, 1,  0, 0, 1, -1]

def bfs():
    while baby_shark:
        x, y = baby_shark.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                baby_shark.append((nx, ny))
                grid[nx][ny] = grid[x][y] + 1
    return


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

baby_shark = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            baby_shark.append((i, j))

bfs()
res = 0
for ii in range(N):
    for jj in range(M):
        if res < grid[ii][jj]:
            res = grid[ii][jj]

print(res-1)