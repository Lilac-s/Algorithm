import sys
sys.stdin= open('sample_input.txt')

'''T = int(input())

for tc in range(1, T+1):
    std = int(input()) # = len(room)
    room = [list(map(int, input().split())) for _ in range(std)]
    # print(room)

    for i in range(std):
        lst = []
        s = room[i][0]
        e = room[i][1]
        for j in range(s, e+1, 1):
            lst.append(j)
        room[i] = lst
    print(room)

    # # 몇 번 반복할지 찾는 식. c번 반복한다.
    # a = std//2
    # b = std%2
    # if b == 1:
    #     c = std*a
    # elif b == 0:
    #     c = std*(a-1) + a
    #
    cnt = 0
    # print(set(room[0]) & set(room[1]))
    # print(bool(set(room[0]) & set(room[1])))
    
    for ii in range(std):
        for jj in range(std):
            if ii != jj and bool(set(room[ii]) & set(room[jj])) == True:
                cnt += 1
            # if set(room[ii]) & set(room[jj]) in room[jj]:
            #     cnt += 1

    if cnt > std:
        print(f'#{tc} {std}')
    elif 0 < cnt <= std:
        print(f'#{tc} {cnt//2 + 1}')
    elif cnt == 0:
        print(f'#{tc} {1}')
'''
t = int(input())

for _ in range(1, t+1):
    n = int(input())  # 학생 수
    room = [0] * 400
    result = 0

    for i in range(n):
        a, b = map(int, input().split())
        if a < b:
            start = a
            end = b
        else:
            start = b
            end = a

        for j in range(start, end):
            room[j] += 1
    # print(room)
    for k in range(len(room)):
        if result < room[k]:
            result = room[k]
    print(f'#{_} {result}')

