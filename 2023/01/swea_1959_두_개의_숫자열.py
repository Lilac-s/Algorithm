T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    dif = abs(len(Ai)-len(Bj))
    res = 0
    if len(Ai) >= len(Bj):
        for i in range(dif+1):
            cnt = 0
            for j in range(len(Bj)):
                cnt += Ai[i+j]*Bj[j]
            if res < cnt:
                res = cnt
    else:
        for i in range(dif+1):
            cnt = 0
            for j in range(len(Ai)):
                cnt += Ai[j]*Bj[i+j]
            if res < cnt:
                res = cnt
    print(f'#{tc} {res}')