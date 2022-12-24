from sys import stdin

N = int(stdin.readline())
score_a = 0
score_b = 0

for _ in range(N):
    A, B = map(int, stdin.readline().split(" "))
    if A > B:
        score_a += 1
    if B > A:
        score_b += 1

print(score_a, score_b)