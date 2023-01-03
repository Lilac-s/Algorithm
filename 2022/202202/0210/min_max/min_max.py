import sys
sys.stdin= open('1.txt')

t = int(input())
for _ in range(t):

    n = int(input())
    ai_lst = list(map(int, input().split()))

    for i in range(n):
        for j in range(len(ai_lst)-1):
            if ai_lst[j] > ai_lst[j+1]:
                ai_lst[j], ai_lst[j+1] = ai_lst[j+1], ai_lst[j]
    print(f'#{_+ 1} {ai_lst[n-1] - ai_lst[0]}')
