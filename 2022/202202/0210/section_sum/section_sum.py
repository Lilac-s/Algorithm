import sys
sys.stdin= open('sample_input(1).txt')

t = int(input()) # 테스트케이스 수 입력받기
for _ in range(t): # 테스트케이스 수만큼 반복하는 반복문 작성

    n, m = map(int, input().split()) # n = 정수의 개수, m = 구간의 개수
    ai_lst = list(map(int, input().split())) # n 개의 정수 ai 리스트

    # n 개의 정수에서 m 의 크기를 가지는 구간의 개수는 n-m+1이다.
    # 10개의 정수를 3개로 묶으면 묶은 덩어리는 총 8개 (10-3+1) 가 된다.
    sum_lst = [0]*(n-m+1) # 이웃한 m개의 합을 전달받을 리스트 생성

    for i in range(n-m+1): # sum_lst에 합을 인덱싱하여 전달할 i 인자의 for문 생성
        for j in range(m): # sum_lst[i]에 구간 m만큼 합을 더해줄 for문 생성
            sum_lst[i] = sum_lst[i] + ai_lst[i + j] # i = 0, sum_lst[0] = ai_lst[0] + ai_lst[1] + ai_lst[2] ...(반복)

    print(f'#{_+1} {max(sum_lst) - min(sum_lst)}') # 출력

