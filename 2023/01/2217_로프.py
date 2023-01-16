N = int(input())
lst = list(int(input()) for _ in range(N))
lst.sort()
res = 0
for i in range(N):
    if lst[i] * (N-i) > res:
        res = lst[i] * (N-i)
print(res)