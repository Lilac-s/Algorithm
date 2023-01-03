import sys
sys.stdin= open('input1.txt')

T = int(input())

for test in range(1, T+1):
    N = int(input()) # 수열의 길이
    n_lst = input().split('0') # 수열, 0을 없애고 1만 남긴다.
    len_lst = len(n_lst)
    res_lst = []
    for i in range(len_lst):
        if len(n_lst[i]) >= 1:
            res_lst.append(n_lst[i])

    res = []
    for j in res_lst:
        for k in range(len(j)):
            res.append(k)
    print(f'#{T} {max(res)+1}')


