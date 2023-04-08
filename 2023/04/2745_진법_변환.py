# 파이썬은 두줄로 풀 수 있다
a, b = input().rstrip().split()
print(int(a, int(b)))

'''
from string import ascii_uppercase

system = {}
num = 10
for i in ascii_uppercase:
    system[i] = num
    num += 1

N, B = input().split(" ")
B = int(B)
res = 0
for i in range(1, len(N)+1):
    digit = N[-i]
    if digit in system.keys():
        res += system[digit]*(B**(i-1))
    else:
        res += int(digit)*(B**(i-1))
print(res)
'''
