res = 0
for i in range(8):
    row = list(input())
    for j in range(8):
        if i%2 == 0 and j%2 == 0 and row[j] == 'F':
            res += 1
        elif i%2 == 1 and j%2 == 1 and row[j] == 'F':
            res += 1

print(res)