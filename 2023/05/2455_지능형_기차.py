people_cnt = 0
max_cnt = 0
for _ in range(4):
    out, on = map(int, input().split(" "))
    people_cnt -= out
    people_cnt += on
    if people_cnt >= max_cnt:
        max_cnt = people_cnt
print(max_cnt)