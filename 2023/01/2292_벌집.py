'''
1 : 1개
2 ~ 7 : 2개 - 5
8 ~ 19 : 3개 - 11 ( + 6 )
20 ~ 37 : 4개 - 17 ( + 6 )
38 ~ 61 : 5개 - 23 ( + 6 )
62 ~ 91 : 6개 - 29 ( + 6 )
~~
'''
house_num = int(input())
cnt = 1
house_cnt = 1
while house_num > house_cnt:
    house_cnt += 6*cnt
    cnt += 1
print(cnt)
    