graph = [list("0"*100) for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = list(map(int, (input().split(" "))))
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

cnt = 0
for j in range(100):
    cnt += graph[j].count(1)

print(cnt)

"""
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""