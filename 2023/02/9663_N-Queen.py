import sys

def dfs(n):
    if n == N:
        global res
        res += 1
    else:
        for i in range(N):
            if visited[i]:
                continue # 아래 코드 건너뛰기
            board[n] = i # (n, i)에 퀸 올리기
            if check(n):
                visited[i] = True
                dfs(n+1)
                visited[i] = False

def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
            return False
    return True
        
N = int(sys.stdin.readline())
res = 0
board = list(0 for _ in range(N))
visited = [False for _ in range(N)]
dfs(0)
print(res)

# def dfs(x, y, cnt):
#     global res
#     if cnt == N:
#         res += 1
#         return
#     for i in range(N):
#         board[x][i] = 1
#         board[y][i] = 1
#         if 0<=x-i<N and 0<=y-i<N:
#             board[x-i][y-i] = 1
#         if 0<=x+i<N and 0<=y+i<N:
#             board[x+i][y+i] = 1
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] != 1:
#                 dfs(i, j, cnt+1)

# N = int(input())
# board = list([0]*N for _ in range(N))
# res = 0
# for i in range(N):
#     for j in range(N):
#         dfs(i, j, 1)
# print(res)