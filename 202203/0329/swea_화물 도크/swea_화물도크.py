import sys
sys.stdin= open('sample_input(3) (1).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_lst = []
    for i in range(N):
        a, b = map(int, input().split())
        time_lst.append([b, a])
    time_lst.sort()
    time_lst.reverse()

    end_time = time_lst.pop()[0]
    cnt = 1
    while time_lst:
        end, start = time_lst.pop()
        if end_time <= start:
            end_time = end
            cnt += 1

    print(f'#{tc} {cnt}')

    # for문으로 하면 reverse pop 으로 안 해도 된다!