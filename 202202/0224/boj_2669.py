grid = [[0]*100 for g in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

    cnt = 0
    for a in grid:
       cnt += sum(a)

print(cnt)