def dfs(depth, idx):
    # depth : 지금 몇명을 뽑았는지 확인하기 위함
    global min_diff
    if depth == N//2:
        start_power, link_power = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_power += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link_power += graph[i][j]
        min_diff = min(min_diff, abs(start_power-link_power))
        return # 절반을 뽑았으면 for 문 돌고 return으로 끝내기

    # 조합
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

N = int(input())
visited = [False for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
min_diff = 1e9

dfs(0, 0)
print(min_diff)