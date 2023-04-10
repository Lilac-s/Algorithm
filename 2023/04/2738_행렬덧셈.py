N, M = map(int, input().split(" "))
res = []
for i in range(N):
    row = list(map(int, input().split(" ")))
    res.append(row)
for i in range(N):
    row = list(map(int, input().split(" ")))
    for j in range(M):
        res[i][j] += row[j]
for i in range(N):
    print(" ".join(map(str, res[i])))