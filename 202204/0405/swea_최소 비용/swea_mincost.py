from collections import deque
import sys
sys.stdin = open('sample_input(3) (1).txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start_x, start_y):
    distance[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                tmp = 1
                if height[nx][ny] > height[x][y]:
                    tmp += height[nx][ny] - height[x][y]
                if distance[nx][ny] > distance[x][y] + tmp:
                    distance[nx][ny] = distance[x][y] + tmp
                    queue.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    distance = list([1e9]*N for _ in range(N))

    bfs(0, 0)
    print(f'#{tc} {distance[N - 1][N - 1]}')
