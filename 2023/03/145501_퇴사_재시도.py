import sys

n = int(sys.stdin.readline())
days = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+days[i][0], n+1):
        if dp[j] < dp[i] + days[i][1]: # dp[j] 는 그 날의 최댓값.
            dp[j] = dp[i] + days[i][1]

print(dp[-1])
# print(max(dp))