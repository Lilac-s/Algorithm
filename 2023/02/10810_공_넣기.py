N, M = map(int, input().split())
basket = ['0']*(N+1)
for i in range(M):
    i, j, k = map(int, input().split())
    for j in range(i, j+1):
        basket[j] = str(k)
basket.pop(0)
print(" ".join(basket))