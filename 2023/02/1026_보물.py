N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
res = 0
for i in range(N):
    res += A[i]*B[N-i-1]

print(res)