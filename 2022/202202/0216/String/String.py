import sys
sys.stdin= open('test_input.txt', encoding='UTF-8')


for _ in range(10):
    T = int(input())
    p = input() # 찾을 패턴(문자열)
    t = input() # 검색할 문장
    M = len(p)  # 찾을 패턴의 길이
    N = len(t)  # 검색할 문장의 길이

    cnt = 0

    for i in range(N-M+1):
        if t[i:i+M] == p:
            cnt += 1
    print(f'#{_+1} {cnt}')

    



    # print(f'#{T} {res}')


