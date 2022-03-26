import sys
sys.stdin= open('sample_input(2).txt')

'''T = int(input())
for _ in range(T):

    input_lst = list(map(int, input().split()))
    P = input_lst[0]
    Pa = input_lst[1]
    Pb = input_lst[2]

    le = 1
    ri = P

    cnt_a = 0
    cnt_b = 0

    while le <= ri:
        c = int((le+ri)/2)
        if c == Pa:
            cnt_a += 1
        elif c > Pa:
            ri = c -1
        else :
            ri = c + 1
    print(cnt_a)'''


def bi_search(p, key): # 이진탐색을 하는 함수 만들기
    start = 1 # 시작 페이지(left)
    end = p # 끝 페이지(right)
    count = 0 # 몇 번 실행했는지 count 해줄 변수 count 생성
    while start <= end: # 탐색할 페이지가 있는지 확인
        c = (start + end) // 2 # 중간값(c) 할당하기
        count += 1 # 탐색할 때마다 count 하기
        if c == key: # 펼친 중간값이 찾고자 하는 페이지와 같다면
            return count # 몇 번 탐색했는지 count를 반환하기
        elif c < key: # 펼친 중간값이 찾고자 하는 페이지보다 작다면
            start = c # 시작 페이지를 중간값으로 설정해서 다시 이진탐색
        elif c > key: # 펼친 중간값이 찾고자 하는 페이지보다 크다면
            end = c # 끝나는 페이지를 중간값으로 설정해서 다시 이진탐색
    return 'wrong' # 뭔가 잘못되었다


T = int(input()) # 테스트케이스 수 받기
for t in range(1, T + 1): # 테스트케이스 수만큼 반복
    p, a, b = map(int, input().split()) # p : 책의 전체 쪽 수, a : A가 찾을 쪽 번호, b : B가 찾을 쪽 번호
    a_c = bi_search(p, a)
    b_c = bi_search(p, b) # 함수 돌리기

    if a_c < b_c:
        result = 'A'
    elif a_c > b_c:
        result = 'B'
    else:
        result = '0' # 둘이 경쟁해서 누가 이겼는지 판별하는 if문
    print("#{} {}".format(t, result)) # 출력문