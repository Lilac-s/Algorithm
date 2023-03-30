n = int(input())
# 별은 i*2-1개 찍힌다
# 가장 많은 별은 n*2-1개
# 별 앞뒤로는 ((n*2-1) - (i*2-1))//2의 공간이 남는다.
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))