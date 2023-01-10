all = int(input())
cnt = int(input())
summary = 0
for _ in range(cnt):
    money, many = map(int, input().split())
    summary += money*many

if all == summary:
    print('Yes')
else:
    print('No')