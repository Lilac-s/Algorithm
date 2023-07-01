import sys
input = sys.stdin.readline

n = int(input())
mine_map = list(list(input()) for _ in range(n))
res_map = list([0]*n for _ in range(n))
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

for i in range(n):
    for j in range(n):
        now = mine_map[i][j]
        if now != '.':
            res_map[i][j] = '*'
        else:
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n and mine_map[x][y] != '.':
                    cnt += int(mine_map[x][y])
            if cnt >= 10:
                res_map[i][j] = 'M'
            else:
                res_map[i][j] = str(cnt)

for i in range(n):
    print("".join(res_map[i]))
