# 카드의 합이 21을 넘지 않는 한도 내에서, 합을 가장 크게 만드는 게임
# N장의 카드 중에서 3장의 카드를 골라, M을 넘지 않으면서 M과 최대한 가깝게 만들기
# 3장의 합을 구해 출력하시오
from itertools import combinations
N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
res = 0
for i in combinations(cards, 3):
    if abs(sum(i)-M) < abs(res-M) and sum(i) <= M:
        res = sum(i)
print(res)


# 아래는 시간 초과가 발생한 코드
'''
def make_sum(depth, cnt, start):
    global res
    if cnt > M:
        return
    if depth >= 3:
        if abs(cnt-M) < abs(res-M):
            res = cnt
            return
    for i in range(start+1, N):
        if cnt + cards[i] < M:
            make_sum(depth+1, cnt+cards[i], i)
    return
    

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
res = 0

for i in range(N):
    make_sum(1, cards[i], i)

print(res)
'''
