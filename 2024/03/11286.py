import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            result = heapq.heappop(heap)
            print(result[1])
        except IndexError:
            print(0)