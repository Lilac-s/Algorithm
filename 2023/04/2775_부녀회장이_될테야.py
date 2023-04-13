t = int(input())
apart = list([1]*15 for _ in range(15))
for i in range(15):
    for j in range(15):
        if i == 0:
            apart[i][j] = j+1
        if j == 0:
            apart[i][j] = 1
        else:
            cnt = 0
            for k in range(j+1):
                cnt += apart[i-1][k]
            apart[i][j] = cnt
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])
