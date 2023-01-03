N, X = map(int, input().split())
Ai = list(map(int, input().split()))

res = []
for i in Ai:
    if i < X:
        res.append(i)

print(*res)