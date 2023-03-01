import sys
import math

# 시험장의 개수
N = int(sys.stdin.readline())
# 각 시험장에 있는 응시자의 수
examinee_lst = list(map(int, sys.stdin.readline().rstrip().split()))
# 총감독관(B명 감시)은 오직 1명, 부감독관(C명 감시)은 여러명
B, C = map(int, sys.stdin.readline().rstrip().split())
res = 0

for i in range(N):
    if examinee_lst[i] <= B:
        res += math.ceil(examinee_lst[i]/B)
    else:
        res += math.ceil((examinee_lst[i] - B)/C) + 1
        
print(res)