import sys
from collections import deque

def bfs(graph, start):
    num = [0]*(n+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:
                num[i] = num[node] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)


n, m = map(int, sys.stdin.readline().strip().split(' '))
# 각 인덱스가 몇 번 노드와 연결되어 있는지 나타내는 그래프
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    graph[x].append(y)
    graph[y].append(x)

results = []
for i in range(1, n+1):
    results.append(bfs(graph, i))

print(results.index(min(results)) + 1)