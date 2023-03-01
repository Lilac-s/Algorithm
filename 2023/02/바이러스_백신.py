import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1. 병원 조합을 만든다.
def make_hos_combi(arr, n):
    result = []
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in make_hos_combi(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

# 2. 각 병원 조합에 맞춰서 bfs를 돌린다.
def clean_virus(hos):
    global min_time
    q = deque([])
    visited = list([0]*N for _ in range(N))
    time_maps = list([0]*N for _ in range(N))

    for h in hos:
        q.append((h[0], h[1], 0))
        visited[h[0]][h[1]] = 1

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] != 1:
                if board[nx][ny] == 0 or board[nx][ny] == 2:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
                    time_maps[nx][ny] = cnt + 1
    time = 0
    for i in range(N):
        for j in range(N):
            # 만일 모든 바이러스를 없애지 못했다면
            if board[i][j] == 0 and time_maps[i][j] == 0:
                # 끝내버린다
                return
            if board[i][j] == 0:
                time = max(time, time_maps[i][j])
    min_time = min(min_time, time)

    # 아래에서 실패하고, 구글링 시작
    # queue = list()
    # queue.append(hos)
    # print(queue)
    # now_time = 0
    # while queue:
    #     node = queue.pop(0)
    #     next_queue = []
    #     for i in range(len(node)):
    #         x = node[i][0]
    #         y = node[i][1]
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if 0<=nx<N and 0<=ny<N:
    #                 if visited[nx][ny] == 0 and board[nx][ny] == 0:
    #                     visited[nx][ny] = -1
    #                     board[nx][ny] = -1
    #                     next_queue.append((nx, ny))
    #     now_time += 1
    #     queue.append(next_queue)
    # # 3. 최소값을 저장해두고, 최소값보다 커지면 bfs를 종료한다.
    # if now_time < min_time:
    #     min_time = now_time
    #     return
    # else:
    #     return
    
# 0 : 바이러스, 1 : 벽, 2 : 병원
N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
hospitals = []
min_time = 1e9 # 바이러스를 없애는 데 걸리는 시간

for i in range(N):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(numbers)
    for j in range(N):
        if numbers[j] == 2:
            hospitals.append((i, j))
            
hos_combi = make_hos_combi(hospitals, M) # 병원 조합

for i in range(len(hos_combi)):
    clean_virus(hos_combi[i])

# 4. 저장된 최소값을 출력한다.
print(-1) if min_time == 1e9 else print(min_time)