import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and field[ny][nx] == 1:
            field[ny][nx] = -1
            dfs(nx, ny)
    #     if 0<=nx<N and 0<=ny<M and field[nx][ny] == 0 and i == 3:
    #         return True
    # return False

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    field = list([0]*M for _ in range(N))
    cnt = 0
    for j in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if field[j][i] == 1:
                dfs(i, j)
                # if dfs(i, j) == True:
                cnt += 1
    print(cnt)