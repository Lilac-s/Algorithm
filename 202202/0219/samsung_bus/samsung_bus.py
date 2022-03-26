import sys
sys.stdin= open('s_input.txt')

'''T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB_lst = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C_lst = [int(input()) for __ in range(P)]

    P_lst = [0]*P
    # print(P_lst)
    # print(AB_lst)
    s = 0
    i = 0

    for i in range(len(AB_lst)):
        s = AB_lst[i][0]
        while i < len(AB_lst):
            P_lst[s-1] += 1
            s += 1
            if s == AB_lst[i][1]+1:
                break

    P_lst = [str(a) for a in P_lst]
    print(f'#{tc} {" ".join(P_lst)}')'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [list(map(int, input().split())) for _ in range(N)]
    # 각각의 버스 구간을 리스트로 저장
    P = int(input())
    C = [int(input()) for _ in range(P)]
    cnt = [0] * 5001  # 각 정류장별로 지나가는 버스 카운트

    for interval in stop:
        for j in range(interval[0], interval[1] + 1):
            cnt[j] += 1
    print(f'#{tc}', end='')
    for num in C:
        print(f' {cnt[num]}', end='')
    print()

# ????