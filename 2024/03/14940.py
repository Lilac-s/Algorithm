import sys
from collections import deque
input = sys.stdin.readline

def find_dist(x, y):
    global result
    queue = deque([])
    queue.append((x, y, 1))
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == True and chart[nx][ny] == 1:
                visited[nx][ny] = False
                result[nx][ny] = min(result[nx][ny], cnt)
                queue.append((nx, ny, cnt+1))
    return

n, m = map(int, input().split(' '))
chart = list()
visited = list([True]*m for _ in range(n))
result = list([1e9]*m for _ in range(n))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(m):
        if row[j] == 2:
            result[i][j] = 0
            target_point = (i, j)
            visited[i][j] = False
        if row[j] == 0:
            result[i][j] = 0
            visited[i][j] = False
    chart.append(row)

find_dist(target_point[0], target_point[1])

for i in range(n):
    for j in range(m):
        if result[i][j] == 1e9:
            result[i][j] = -1
    print(' '.join(map(str, result[i])))