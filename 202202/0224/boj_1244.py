n = int(input()) # <= 100

switch = list(map(int,input().split())) # 스위치
n = len(switch)
# 인덱스와 번호를 일치시키기, 0, 1을 안쓰는 이유는 여성일 경우를 따로 처리해줘야해서
switch = [-1] + switch

num_student = int(input())

# student = [list(map(int,input().split())) for _ in range(num_student)]

def func(i):
    if switch[i] == 0:
        switch[i] = 1
    elif switch[i] == 1:
        switch[i] = 0



for _ in range(num_student):
    gender, num = map(int,input().split())

    #남자일때는 ~~~
    if gender == 1:
        for i in range(num,n+1):
            if i % num == 0:
                func(i)
        # print(switch, '남자 다음 스위치')

    #여자일때는~~
    elif gender == 2:
        # num 기준으로 대칭인 아이들의 상태를 바꾸겠어
        switch[num] = not switch[num]
        k = 1
        while 1:
            if num - k >= 1 and num + k <= n:
                if switch[num - k] == switch[num + k]:
                    switch[num - k] = not switch[num - k]
                    switch[num + k] = not switch[num + k]
                else:
                    break
            else:
                break
            k += 1
        #     print(switch, num,  k, "여자 while 안쪽")
        # print(switch, '여자 다음 스위치')

switch = list(map(int,switch))
print(*switch[1:])