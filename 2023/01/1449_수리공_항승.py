# 직접 손으로 그리고 써보는게 중요하다는걸 다시 한번 알게 된 문제.

N, L = map(int, input().split())
leak_lst = list(map(int, input().split()))
# 앞에서부터 테이프를 붙여나가야 하므로 정렬해주었다.
leak_lst.sort()
pipe = list(0 for _ in range(1001))
cnt = 0

for i in range(N):
    leak_place = leak_lst[i]
    if pipe[leak_place] == 0:
        for j in range(L):
            if leak_place + j <= 1000:
                pipe[leak_place + j] = 1
        cnt += 1

print(cnt)

# 0.5단위를 보고 2000개 리스트를 만들어야 한다는 이상한 착각을 했었다.
# import math

# N, L = map(int, input().split())
# place = list(map(int, input().split()))
# pipe = list('0' for _ in range(2000))

# for i in place:
#     if i != 0:
#         pipe[i*2-1] = '1'
#         pipe[i*2] = '1'
#         pipe[i*2+1] = '1'
#     if i == len(place):
#         pipe[len(place)-1] = '1'
#         pipe[len(place)-2] = '1'
#     if i == 0:
#         pipe[0] = '1'
#         pipe[1] = '1'

# need_tape = []
# cnt = 0
# for j in range(len(pipe)):
#     if pipe[j] == '1':
#         need_tape.append('1')
#     if pipe[j] == '0' and len(need_tape) != 0:
#         length = L*2+1
#         cnt += math.ceil(len(need_tape)/length)
#         need_tape = []

# print(cnt)