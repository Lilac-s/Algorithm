N = list(input())
A = str(''.join(N))

if len(N) < 2:
    N = ['0'] + N

cnt = 0
while 1:
    Ni = int(N[0]) + int(N[1])
    if len(str(Ni)) < 2:
        Ni = '0' + str(Ni)
    N = N[1] + str(Ni)[-1]
    cnt += 1
    if N == A:
        break

print(cnt)
