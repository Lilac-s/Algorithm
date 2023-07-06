n = int(input())
trophy_lst = list(int(input()) for _ in range(n))
cnt_l = 0
cnt_r = 0
high = 0

for i in trophy_lst:
    if i > high:
        high = i
        cnt_l += 1

high = 0
for j in trophy_lst[::-1]:
    if j > high:
        high = j
        cnt_r += 1

print(cnt_l)
print(cnt_r)
