import sys
sys.stdin= open('sample_input.txt')

def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper(N-10) + 2*paper(N-20) # 등차수열으로 수가 커진다

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = paper(N)
    print(f'#{tc} {res}')