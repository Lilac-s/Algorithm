from collections import deque

n = int(input())
lst = list(map(int, input().split()))
visited = [-1]*n #방문할 때마다 점프 횟수를 기록

def bfs(start):
    queue = deque([start])
    visited[start] = 0 #0으로 세기 시작
    while queue:
        v = queue.popleft()
        jump = lst[v] #lst의 첫번째에서 점프 시작
        for i in range(jump, 0, -1):
            if v + i < n and visited[v + i] == -1: #Ai 이하만큼 오른쪽으로 떨어진 칸 중에 가장 큰 수 찾기
                visited[v + i] = visited[v] + 1 #이전에 점프한 횟수 + 1 을 점프한 곳에 기록
                queue.append(v + i) # 큐에 점프한 거리 append 해서 넣기
    # while문이 돌아가면서 점프한 거리를 다시 popleft해서 사용하므로
    # 이 다음 점프할 때 이미 점프했던 위치에서 점프하게 된다.

bfs(0)
print(visited[-1])
