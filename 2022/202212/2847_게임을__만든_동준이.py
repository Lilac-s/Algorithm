N = int(input())
scores = list(int(input()) for _ in range(N))

cnt = 0
for i in range(len(scores)-1):
    while scores[N-i-2] >= scores[N-i-1]:
        scores[N-i-2] -= 1
        cnt += 1
print(cnt)