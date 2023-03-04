import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, depth, cal):
    global max_value
    if depth == 4:
        max_value = max(max_value, cal)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, depth+1, cal+board[ny][nx])
            visited[ny][nx] = False

def exc_cal(x, y):
    global max_value
    exc_value = board[y][x]
    exc_case = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    for i in range(4):
        for j in range(3):
            nx = x + dx[exc_case[i][j]]
            ny = y + dy[exc_case[i][j]]
            if 0<=nx<m and 0<=ny<n:
                exc_value += board[ny][nx]
        max_value = max(exc_value, max_value)
        exc_value = board[y][x]

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_value = 0

for i in range(m):
    for j in range(n):
        visited[j][i] = True
        dfs(i, j, 1, board[j][i])
        visited[j][i] = False
        exc_cal(i, j)

print(max_value)