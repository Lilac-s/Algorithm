import math

n = int(input())
size = list(map(int, input().split(' ')))
t, p = map(int, input().split(' '))

shirt = 0
for i in range(6):
    shirt += math.ceil(size[i]/t)
    
print(shirt)
print(n//p, n%p)