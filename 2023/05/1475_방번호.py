import math

num = input()
cnt_lst = [0]*10
for i in num:
    number = int(i)
    cnt_lst[number] += 1
cnt_lst[6] += cnt_lst[9]
cnt_lst[9] = 0
cnt_lst[6] = math.ceil(cnt_lst[6]/2)
print(max(cnt_lst))