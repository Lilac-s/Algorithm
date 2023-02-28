#이제 *에서 시작해서 탐색해보자.
# 됐다 !!!
def click(x, y):
    board[x][y] = 'checked'
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny] == 'near':
                board[nx][ny] = 'checked'
            if board[nx][ny] == '.':
                click(nx, ny)

def near_the_mine(x, y):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == '.':
            board[nx][ny] = 'near'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    visited = list([0]*N for _ in range(N))
    cnt = 0
    for i in range(N):
        board.append(list(input()))
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                near_the_mine(i, j)
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt += 1
                click(i, j)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'near':
                cnt += 1
    print(f'#{tc} {cnt}')

# 아래는 .에서부터 시작했다.
# from pprint import pprint

# def dfs(x, y):
#     dx = [0, 0, 1, -1, 1, 1, -1, -1]
#     dy = [1, -1, 0, 0, 1, -1, 1, -1]
#     cnt = 0
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<= nx < N and 0<= ny < N and board[nx][ny] == '*':
#             cnt += 1
#     if cnt > 0:
#         board[x][y] == cnt
#     if cnt == 0:
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx < N and 0<= ny < N:
#                 board[nx][ny] = 'checked'
#     pprint(board)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     board = []
#     visited = list([0]*N for _ in range(N))
#     click = 0
#     for i in range(N):
#         board.append(list(input()))
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == '.':
#                 board[i][j] = 'checked'
#                 click += 1
#                 dfs(i, j)
#     print(f'#{tc} {click}')