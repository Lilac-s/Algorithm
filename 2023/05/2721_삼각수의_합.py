import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    num = int(input())
    sum = 0
    w = 0
    for j in range(1, num+1):
        for k in range(1, j+2):
            w += k
        sum += j*w
        w = 0
    print(sum)