n = int(input())
cnt = 1
res = 0
while n > 0:
    if n < cnt:
        cnt = 1
    n-= cnt
    cnt += 1
    res += 1
print(res)