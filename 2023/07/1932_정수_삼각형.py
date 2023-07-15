n = int(input())  # 삼각형의 크기를 입력받음
dp = []  # DP 테이블을 저장할 리스트

# 입력값을 이차원 리스트 형태로 dp 테이블에 저장하기
for i in range(n):
    dp.append(list(map(int, input().split())))

# 삼각형의 위에서부터 아래로 내려가며 최댓값 계산
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] += dp[i - 1][0]  # 첫 열의 경우, 바로 위의 값과 더하여 최댓값 갱신
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]  # 마지막 열의 경우, 왼쪽 위의 값과 더하여 최댓값 갱신
        else:
            # 그 외의 경우, 두 값 중 큰 값과 더하여 최댓값 갱신
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

# 마지막 행에서의 최댓값 출력
print(max(dp[n - 1]))
