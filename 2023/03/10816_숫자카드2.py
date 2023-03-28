import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split(" ")))
M = int(input())
find_numbers = list(map(int, input().split(" ")))
numbers.sort()

def count_by_range(a, l, r):
    right_index = bisect_right(a, r)
    left_index = bisect_left(a, l)
    return right_index - left_index

for i in range(len(find_numbers)):
    print(count_by_range(numbers, find_numbers[i], find_numbers[i]), end=" ")