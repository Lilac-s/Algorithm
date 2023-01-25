N = int(input())
numbers = map(int, input().split())
cnt = N

for x in numbers:
    if x == 1:
        cnt -= 1
    for j in range(2, x):
        if x % j == 0:
            cnt -= 1
            break

print(cnt)