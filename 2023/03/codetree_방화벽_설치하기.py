# 불 : 2, 벽 : 1, 빈칸 : 0
# 불이 퍼지지 않은 영역 출력
import sys
from collections import deque
from pprint import pprint
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# visited 배열 초기화
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

# dfs로 방화벽 조합 백트래킹 (백트래킹? 이걸 백트래킹이라고 할 수 있나?)
def dfs(depth):
    global max_place
    if depth == 3:
        protected_place = bfs()
        max_place = max(max_place, protected_place)
        return
    else:
        for i in range(n):
            for j in range(m):
                if place[i][j] == 0:
                    place[i][j] = 1
                    dfs(depth+1)
                    place[i][j] = 0

# bfs로 불 지르고, 퍼지지 않은 영역 return
def bfs():
    fired = deque()
    fired.extend(fire_place)
    # bfs를 여러 번 호출한다면, visited를 꼭 초기화해주자.
    initialize_visited()
    while fired:
        x, y = fired.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스를 잘 보자!
            if 0<=nx<n and 0<=ny<m and place[nx][ny] == 0 and not visited[nx][ny]:
                fired.append((nx, ny))
                visited[nx][ny] = True
    not_fired = 0
    for i in range(n):
        for j in range(m):
            if place[i][j] == 0 and not visited[i][j]:
                not_fired += 1
    return not_fired

n, m = map(int, sys.stdin.readline().rstrip().split())
place = []
visited = [[False]*m for _ in range(n)]
fire_place = []
max_place = 0

for i in range(n):
    status = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        if status[j] == 2:
            fire_place.append((i, j))
            visited[i][j] = True
    place.append(status)

for i in range(n):
    for j in range(m):
        if place[i][j] == 0:
            place[i][j] = 1
            dfs(1)
            place[i][j] = 0

print(max_place)