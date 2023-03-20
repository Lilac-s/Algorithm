A, B = map(int, input().split(" "))
big_num = max([A, B])
small_num = min([A, B])
# 최대공약수 구하기
gcd = 1
for i in range(2, small_num+1):
    if A%i == 0 and B%i == 0:
        if i > gcd:
            gcd = i

# 최소공배수 구하기
lcm = 0
lst = []
i = 0
while 1:
    i += 1
    lst.append(big_num*i)
    if small_num*i in lst:
        lcm = small_num*i
        break

print(gcd)
print(lcm)