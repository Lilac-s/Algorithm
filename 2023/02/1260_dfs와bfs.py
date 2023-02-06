from collections import deque

def dfs(n):
    dfs_visited[n] = True
    dfs_lst.append(n)
    for i in graph[n]:
        if dfs_visited[i] == False:
            dfs(i)

def bfs(n):
    bfs_visited[n] = True
    bfs_lst.append(n)
    queue = deque()
    queue = [n]
    while queue:
        for i in graph[queue.pop(0)]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                bfs_lst.append(i)
                queue.append(i)

N, M, V = map(int, input().split())
graph = list([] for _ in range(N+1))

dfs_visited = [False]*(N+1)
bfs_visited = [False]*(N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in range(N+1):
    graph[j].sort()

dfs_lst = []
bfs_lst = []

dfs(V)
bfs(V)
print(" ".join(map(str, dfs_lst)))
print(" ".join(map(str, bfs_lst)))