n = int(input())
marking = list(map(int, input().split(" ")))
cnt = 0
res = 0
for i in range(n):
    if marking[i] == 0:
        cnt = 0
    elif marking[i] == 1:
        cnt += 1
        res += cnt
print(res)