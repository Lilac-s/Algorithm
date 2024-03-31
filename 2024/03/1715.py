import sys, heapq

input = sys.stdin.readline
n = int(input())
cards = list(int(input()) for _ in range(n))
heapq.heapify(cards)
res = 0

if len(cards) == 1:
    print(res)
else:        
    while len(cards) >= 2:
        card = heapq.heappop(cards)
        compare_card = heapq.heappop(cards)
        res += card + compare_card
        heapq.heappush(cards, card+compare_card)
    print(res)