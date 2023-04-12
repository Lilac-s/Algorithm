import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lengths = list()
for i in range(k):
    lengths.append(int(input()))
start = 1
end = max(lengths)
while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += lengths[i] //mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)