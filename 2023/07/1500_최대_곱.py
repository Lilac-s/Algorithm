import sys

n, m = map(int, sys.stdin.readline().split())
p = n // m  # 몫을 구함
q = n % m   # 나머지를 구함
ans = 1     # 결과를 저장할 변수 초기화

for _ in range(m):
    if q > 0:
        ans *= (p + 1)  # 나머지가 있는 경우, 몫에 1을 더한 값을 곱함
        q -= 1          # 나머지 처리를 위해 나머지 값 감소
    else:
        ans *= p        # 나머지가 없는 경우, 몫을 곱함

print(ans)
