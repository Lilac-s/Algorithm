# 재귀 이용
# DP와 비교했을 때 약 2배의 시간 소요
def cal(x, cnt):
    global res
    if cnt > res:
        return
    if x == 1:
        res = cnt
    if x%3 == 0:
        cal(x//3, cnt+1)
    if x%2 == 0:
        cal(x//2, cnt+1)
    cal(x-1, cnt+1)

x = int(input())
res = 1e9
cal(x, 0)
print(res)

# DP
# n만큼의 리스트 생성, 답을 기록하는 방식
n = int(input())
dp = [0] * 1000001

for i in range(2, n+1):
    # bottom-up 방식
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])