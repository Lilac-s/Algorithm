import sys
sys.stdin= open('sample_input(1).txt')

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)

    subset = [] # 모든 부분집합을 받을 리스트 생성

    for i in range(1<<n): # 1<<n : 부분 집합의 개수 2^n
        subset_lst = [] # 만들어진 부분집합 하나하나를 받을 리스트 생성
        for j in range(n): # 원소의 수만큼 비트를 비교한다.
            if i & (1<<j): # i의 j번 비트가 1인 경우 부분집합의 원소가 된다.
                subset_lst.append(arr[j]) # 원소를 subset_lst에 append 해준다.
        subset.append(subset_lst) # 만들어진 부분집합을 subset에 append 해준다.

    cnt = 0
    for sub in subset:
        if len(sub) == N and sum(sub) == K: # 문제 조건에 맞으면
            cnt += 1 # 카운트해준다.


    print(f'#{_+1} {cnt}')

