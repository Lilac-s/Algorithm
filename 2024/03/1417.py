import sys, heapq

input = sys.stdin.readline
n = int(input())
vote_cnt = []
dasom_cnt = int(input())
buy_cnt = 0

for _ in range(1, n):
    cnt = int(input())
    heapq.heappush(vote_cnt, (-cnt, cnt))

while vote_cnt and dasom_cnt <= vote_cnt[0][1]:
    num = heapq.heappop(vote_cnt)[1]
    dasom_cnt += 1
    num -= 1
    buy_cnt += 1
    heapq.heappush(vote_cnt, (-num, num))

print(buy_cnt)