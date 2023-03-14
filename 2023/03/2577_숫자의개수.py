res = 1
for i in range(3):
    res *= int(input())
res_lst = list(str(res))
for i in range(10):
    print(res_lst.count(str(i)))