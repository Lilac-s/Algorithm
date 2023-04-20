n = int(input())
times = list(map(int, input().split(" ")))
Y = 0
M = 0
for i in times:
    Y += i // 30 * 10 + 10
    M += i // 60 * 15 + 15
if M < Y:
    print('M', M)
elif Y < M:
    print('Y', Y)
elif Y == M:
    print('Y M', Y)