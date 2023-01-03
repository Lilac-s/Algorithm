import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

queue = deque()
for i in range(M):
    for j in range(N):
        if graph[j][i] == 1:
            queue.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

bfs() #???

max_value = 0
for i in range(M):
    for j in range(N):
        if graph[j][i] == 0:
            print(-1)
            exit()
        else:
            if max_value < graph[j][i]:
                max_value = graph[j][i]
print(max_value - 1)