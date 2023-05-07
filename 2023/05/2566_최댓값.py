x = 1
y = 1
res = 0
for i in range(1, 10):
    row = list(map(int, input().split(" ")))
    for j in range(9):
        if row[j] >= res:
            res = row[j]
            x = i
            y = j + 1
print(res)
print(x, y)