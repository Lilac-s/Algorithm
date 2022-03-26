from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    tmp = []
    while q:
        r, c = q.popleft()
        arr[r][c] = -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < height and 0 <= nc < width:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1
                    q.append((nr, nc))
                if arr[nr][nc] == 1 and arr[r][c] == -1:
                    tmp.append((nr, nc))
    return tmp


height, width = map(int, input().split())
arr = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for _ in range(height):
    arr.append(list(map(int, input().split())))

cnt = 1
cheese = deque(set(bfs(0, 0)))

while True:
    tmp = []
    last = len(cheese)
    while cheese:
        for side in cheese:
            r, c = side[0], side[1]
            arr[r][c] = 0
        r, c = cheese.popleft()
        tmp += bfs(r, c)
    if tmp == []:
        break
    else:
        cheese = deque(set(tmp))
        cnt += 1

print(cnt, last, sep='\n')