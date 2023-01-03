
# LIS (Longest Increasing Subsequence, 가장 긴 증가하는 부분수열)를 이용하는 문제.
# 주어진 배열에서 가장 길게 증가하는 부분 수열을 찾아내고,
# 그 배열을 제외한 나머지를 옮기면 번호 순서대로 줄을 세울 수 있다.
# 따라서 배열을 제외한 나머지가 정답이 된다.

n = int(input())

d = [1]*(n+1)
kid = [0]
for i in range(n):
    kid.append(int(input()))

for i in range(1, n+1):
    for j in range(1, i):
        if kid[j] < kid[i]:
            d[i] = max(d[i], d[j] + 1)

print(n-max(d))