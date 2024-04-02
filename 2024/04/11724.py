import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(n):
    queue = deque([n])
    visited[i] = False
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node]:
                queue.append(next_node)
                visited[next_node] = False

# def dfs(node):
#     visited[node] = False
#     for next_node in graph[node]:
#         if visited[next_node]:
#             dfs(next_node)
#     return

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
visited = [True]*(n+1)
cnt = 0
for _ in range(m):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    # if not graph[i]:
    #     visited[i] = False
    #     cnt += 1
    # if graph[i] and visited[i]:
    if visited[i]:
        cnt += 1
        # dfs(i)
        bfs(i)
print(cnt)

'''
처음에 33번 라인에 `if graph[i] and visited[i]`로 작성했다가 많이 헤맸다.
graph[i] 가 비어 있으면 bfs 또는 dfs함수를 탔을 때 다음 로직 없이 그냥 끝나기 때문에 고려하지 않아도 된다고 생각했는데,
이렇게 하면 해당 node가 visited처리가 되지 않기 때문에 문제가 생기는 거였다. 40%에서 틀렸다고 하더라.
만일 이런 식으로 풀 거라면, graph[i]가 비어 있을 때 따로 visited처리를 해 주어야 한다.
그리고 이렇게 아무것도 연결되지 않은 node는 하나의 연결 요소가 되기 때문에 cnt에도 하나 더해 주어야 한다.
dfs와 bfs 사이에는 크게 시간 차이가 발생하지 않았다.
'''