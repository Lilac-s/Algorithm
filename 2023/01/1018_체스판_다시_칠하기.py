def findcnt(x, y):
    cnt_w = 0
    cnt_b = 0
    for i in range(8):
        for j in range(8):
            if i%2==1 and j%2==0 and board[i+x][j+y] != 'B':
                cnt_w += 1
            if i%2==0 and j%2==1 and board[i+x][j+y] != 'B':
                cnt_w += 1
            if i%2==1 and j%2==1 and board[i+x][j+y] != 'W':
                cnt_w += 1
            if i%2==0 and j%2==0 and board[i+x][j+y] != 'W':
                cnt_w += 1
    for i in range(8):
        for j in range(8):
            if i%2==1 and j%2==0 and board[i+x][j+y] != 'W':
                cnt_b += 1
            if i%2==0 and j%2==1 and board[i+x][j+y] != 'W':
                cnt_b += 1
            if i%2==1 and j%2==1 and board[i+x][j+y] != 'B':
                cnt_b += 1
            if i%2==0 and j%2==0 and board[i+x][j+y] != 'B':
                cnt_b += 1
    return(min(cnt_w, cnt_b))


N, M = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(input()))

res = 1e9
for x in range(N-7):
    for y in range(M-7):
        cnt = findcnt(x, y)
        if cnt < res:
            res = cnt

print(res)