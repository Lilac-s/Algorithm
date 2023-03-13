N = int(input())
for _ in range(N):
    ox_lst = list(input())
    score = 0
    cnt = 0
    for i in range(len(ox_lst)):
        if ox_lst[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)