def backtracking(i, N, s, visited):
    global sumV
    if i == N:
        if s < sumV:
            sumV = s
    elif s > sumV:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtracking(i + 1, N, s + num_list[i][j], visited)
                visited[j] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    sumV = 100
    visited = [0] * N

    backtracking(0, N, 0, visited)
    print(f'#{tc + 1} {sumV}')