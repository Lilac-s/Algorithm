import sys
sys.stdin= open('input.txt')

for _ in range(10): # 총 10개의 테스트케이스

    T = int(input()) # 테스트케이스 번호 받기
    lst = [list(map(int, input().split())) for N in range(100)] # 100*100 리스트 받기

    sum_lst = [] # 행, 열, 대각선의 합을 받을 리스트 만들기

    # 각 행을 더하는 for 문 작성
    for i in range(100): # i : 각각의 행을 지정한다.
        a = 0               # 각각의 합을 저장해 줄 변수 a 선언
        for j in range(100): # j : 행에서 각각의 열 값을 지정한다.
            a += lst[i][j] # lst의 행, 열을 인덱싱하여 변수 a에 더해준다.
        sum_lst.append(a) # 행의 모든 값을 더한 a를 sum_lst에 append 해준다.

    # 각 열을 더하는 for 문 작성, 과정은 위와 같다.
    for j in range(100):
        b = 0
        for i in range(100):
            b += lst[i][j]
        sum_lst.append(b)

    # 대각선을 더하는 for 문 작성.
    c = 0
    d = 0
    for i in range(100):
        c += lst[i][i] # 좌측 위에서 우측 아래로 가는 대각선
        d += lst[i][-i] # 우측 위에서 좌측 아래로 가는 대각선
    sum_lst.append(c)
    sum_lst.append(d)

    for bub in range(100):
        for k in range(len(sum_lst) - 1):  # 버블 정렬
            if sum_lst[k] > sum_lst[k + 1]:
                sum_lst[k], sum_lst[k + 1] = sum_lst[k + 1], sum_lst[k]

    print(f'#{_+1} {sum_lst[-1]}') # 출력

