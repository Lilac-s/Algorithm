import sys
sys.stdin= open('1.txt')
t = int(input()) # 테스트 케이스 개수
for _ in range(t):

    n = int(input()) # 카드 장수
    ai_lst = list(map(int, input())) # n개의 숫자 ai리스트

    # 길이 10의 cnt리스트 생성
    cnt_lst = [0] * 10 # 각각의 위치에 카운트해서 개수를 더해줄 것

    for j in range(n): # 주어진 카드를 확인하는 for 문
        for i in range(1, 10): # 1부터 9까지의 카드 경우의 수를 확인하는 for 문
            if i == ai_lst[j]: # 주어진 카드에 카드 경우의 수가 존재한다면
                cnt_lst[i-1] += 1 # cnt_lst에 인덱싱해서 카드 수를 센다.

    # 위의 코드를 이렇게 줄일 수도 있네
    # for i in ai_lst:
        # cnt_lst[i] += 1

    res_i = 0
    res_cnt = 0 # 결과값을 받을 변수 설정

    for i, cnt in enumerate(cnt_lst): # 인덱싱 값을 출력해야 하므로 enumerate 함수 사용
        if cnt == max(cnt_lst): # cnt_lst에서 가장 큰 값 추출
            res_i = i
            res_cnt = cnt # 각각의 변수에 할당

    print(f'#{_+1} {res_i+1} {res_cnt}') #출력


# 아래는 enumerate 함수를 사용하지 않을 때 헤멘 흔적.
    # mX_cnt = max(cnt_lst)
    #
    # for a in range(-1, 9, -1):
    #     if mX_cnt == cnt_lst[a]:
    #         mx_num = cnt_lst[a]
    #
    # print(f'# {_+1} {cnt_lst[a]} {mx_num}')
