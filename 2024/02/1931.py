import sys

n = int(input())
end_time = 0
res = 0
meetings = list()

for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().strip().split(' '))))

# 끝나는 시간으로 배열을 정렬 - 일찍 끝날수록 많은 회의를 진행할 수 있음
meetings.sort(key=lambda x: (x[1], x[0]))

for start, end in meetings:
    if end_time <= start:
        res += 1
        end_time = end

print(res)