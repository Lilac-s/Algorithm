import sys
sys.stdin= open('sample_input(1).txt')

tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split()) # N * N 크기의 글자판에서 / 길이가 M인 회문을 찾아야 한다.
    let_lst = [list(input()) for a in range(N)]
    result = []

    # 행 회문 찾기
    for i in range(N):
        for k in range(N - M + 1):
            lst = []
            for j in range(M):
                lst.append(let_lst[i][j+k])
            rev_lst = lst[::-1]
            if rev_lst == lst:
                result = rev_lst

    # 열 회문 찾기
    for i in range(N):
        for k in range(N - M + 1):
            lst = []
            for j in range(M):
                lst.append(let_lst[j+k][i])
            rev_lst = lst[::-1]
            if rev_lst == lst:
                result = rev_lst

    print(f'#{_+1} {"".join(result)}')
























'''    for r in range(N):
        for c in range(N-M+1):
            for k in range(M//2):
                if let_lst[i][j+k] == let_lst[i][j+M-1-k]:


# lst[i][j:j+M] == lst[i][j:j+M][::01]
'''


''''tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split()) # N * N 크기의 글자판에서 / 길이가 M인 회문을 찾아야 한다.
    let_lst = [list(input()) for a in range(N)]


    for r in range(N):
        for pal in range(N-M+1):
            if let_lst[r] == reversed(let_lst[r]):
                print(let_lst[r])

    for pal in range(N - M + 1):
        for c in range(N):
            col_lst = []
            for r in range(N):
                col_lst.append(let_lst[r][c])
            if col_lst == col_lst[::-1]:
                print(col_lst)'''



'''    # 행 회문 찾기
    reverse_lst = [[0] * N for A in range(N)]
    for i in range(N):
        for j in range(N):
            reverse_lst[i][-j-1] = let_lst[i][j]
        # print(reverse_lst[i])

        for rev in range(1, N-M+2):
            # print(let_lst[i][:rev+M])
            # print(reverse_lst[i][-rev-M:])
            if let_lst[i][:rev+M] == reverse_lst[i][-rev-M:]:
                print(reverse_lst[i][-rev-M:])
            else:
                print(0)

    # 열 회문 찾기
'''








'''    let_lst = [list(input()) for t in range(M)]
    res_lst = []
    # print(let_lst)

    # 행 회문 찾기
    for i in range(M):
        row_lst = []
        for j in range(M):
            row_lst.append(let_lst[i][-j-1])
        if row_lst == let_lst[i]:
            res_lst.append(row_lst)

    # 열 회문 찾기
    # for ten in range(M):
    #     col_lst = []
    for i in range(M):
        col_lst_reverse = []
        col_lst = []
        for j in range(M):
            col_lst_reverse.append(let_lst[-j-1][i])
            col_lst.append(let_lst[j][i])
        if col_lst == col_lst_reverse:
            res_lst.append(col_lst)

    print(res_lst)
    
    # 이렇게 풀면 길이가 M인 회문을 찾을 수 없다.'''

