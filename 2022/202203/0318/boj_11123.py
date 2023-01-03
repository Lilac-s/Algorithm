def dfs(x, y):
    grid[x][y] = '.' # 양을 풀로 바꿔주기
    for i in range(4):
        X, Y = x+dx[i], y+dy[i] # 왔다갔다하면서
        if (0 <= X < H) and (0 <= Y < W) and grid[X][Y] == '#': # 거기 양이 있다면
            dfs(X, Y) # 다시 dfs를 돌면서 반복

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                dfs(i, j) # 그리드를 순회하다가 양을 만나면 dfs 함수 실행
                cnt += 1
    print(cnt)

    # 왜 런타임 에러가 생길까?