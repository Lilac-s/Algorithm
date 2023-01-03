from collections import deque

def bfs(graph, start, end, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] +1
                if i == end:
                    return distance[i]
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    start, end = map(int, input().split())
    visited = [False]*(V+1)
    distance = [0]*(V+1)

    res = bfs(graph, start, end, visited)
    print(f'#{tc} {res}')