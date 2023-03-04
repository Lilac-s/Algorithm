import sys

def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        start_power, link_power = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_power += board[i][j]
                elif not visited[i] and not visited[j]:
                    link_power += board[i][j]
        min_diff = min(min_diff, abs(start_power-link_power))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [False for _ in range(n)]
min_diff = 1e9
dfs(0, 0)
print(min_diff)