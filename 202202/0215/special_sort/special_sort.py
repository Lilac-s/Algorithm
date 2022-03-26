import sys
sys.stdin= open('sample_input(3).txt')

T = int(input())
for _ in range(T):

    N = int(input())
    ai_lst = list(map(int, input().split()))

    for i in range(N):
        for j in range(len(ai_lst) - 1):  # 버블 정렬
            if ai_lst[j] > ai_lst[j + 1]:
                ai_lst[j], ai_lst[j + 1] = ai_lst[j + 1], ai_lst[j]

    res_lst = []
    mx = 0
    mn = 0

    while len(ai_lst) >= 1:
        mx = ai_lst.pop(-1)
        res_lst.append(mx)

        mn = ai_lst.pop(0)
        res_lst.append(mn)

    print(f'#{_+1} {" ".join(map(str, res_lst[0:10]))}')







'''
res_lst = []
i = 0

while i <= N:
            i = 0
            if ai_lst[i] == max(ai_lst):
                mx = ai_lst.pop(i)
                res_lst.append(mx)
                i += 1
    
            elif ai_lst[i] == min(ai_lst):
                mn = ai_lst.pop(i)
                res_lst.append(mn)
                i += 1

print(res_lst)
'''

