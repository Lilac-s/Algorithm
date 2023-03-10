N, M = map(int, input().split())
baskets = list()
for i in range(1, N+1):
    baskets.append(i)
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])
print(" ".join(map(str, baskets)))