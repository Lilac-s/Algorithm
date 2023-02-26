N, M = map(int, input().split())
baskets = []
for i in range(N+1):
    baskets.append(str(i))

for j in range(M):
    i, j = map(int, input().split())
    a = baskets[i]
    b = baskets[j]
    baskets[j] = a
    baskets[i] = b

print(" ".join(baskets[1:]))