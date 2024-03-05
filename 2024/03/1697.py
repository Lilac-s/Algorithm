from collections import deque

def bfs():
    queue = deque([])
    queue.append(n)
    while queue:
        l= queue.popleft()
        if l == k:
            return visited[l]
        # (l-1, l+1, l*2)에서 l*2가 앞서서 나오면 안 됨
        # 2*l이 먼저 큐에 들어가는 경우, l+1, l-1을 고려하지 못하는 경우가 생길 수 있음.
        # 하지만 그 역은, l*2가 이미 큐에 들어가 있기 때문에 고려 가능함.
        # 따라서 bfs에서는 큐에 어떠한 순서대로 넣어야 안전하게 경우를 탐색할 수 있을지 생각할 필요가 있음.
        for j in (l-1, l+1, l*2):
            if 0<=j<100001 and not visited[j]:
                visited[j] = visited[l] + 1
                queue.append(j)

n, k = map(int, input().split(' '))
visited = [0]*100001
print(bfs())