t = int(input())

for _ in range(t):
    N = int(input())
    sum_c = 0
    sum_g = 0
    
    for _ in range(N):
        c, g = map(float, input().split())
        sum_c += c
        sum_g += c * g
        
    gpa = sum_g / sum_c
    print(int(sum_c), '%.1f' % gpa)