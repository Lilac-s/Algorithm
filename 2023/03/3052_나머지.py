res = []

for i in range(10):
    left = int(input())%42
    if left not in res:
        res.append(left)

print(len(res))