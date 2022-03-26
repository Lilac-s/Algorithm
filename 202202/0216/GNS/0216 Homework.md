# 0216 Homework



## GNS



```python
import sys
sys.stdin= open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    tc, a = input().split()
    tc_len = int(a)
    tc_lst = list(input().split())
    # print(tc)
    # print(tc_len)
    # print(tc_lst)
    for i in range(tc_len):
        if tc_lst[i] == 'ZRO':
            tc_lst[i] = 0
        if tc_lst[i] == 'ONE':
            tc_lst[i] = 1
        if tc_lst[i] == 'TWO':
            tc_lst[i] = 2
        if tc_lst[i] == 'THR':
            tc_lst[i] = 3
        if tc_lst[i] == 'FOR':
            tc_lst[i] = 4
        if tc_lst[i] == 'FIV':
            tc_lst[i] = 5
        if tc_lst[i] == 'SIX':
            tc_lst[i] = 6
        if tc_lst[i] == 'SVN':
            tc_lst[i] = 7
        if tc_lst[i] == 'EGT':
            tc_lst[i] = 8
        if tc_lst[i] == 'NIN':
            tc_lst[i] = 9

    tc_lst.sort()

    for i in range(tc_len):
        if tc_lst[i] == 0:
            tc_lst[i] = 'ZRO'
        if tc_lst[i] == 1:
            tc_lst[i] = 'ONE'
        if tc_lst[i] == 2:
            tc_lst[i] = 'TWO'
        if tc_lst[i] == 3:
            tc_lst[i] = 'THR'
        if tc_lst[i] == 4:
            tc_lst[i] = 'FOR'
        if tc_lst[i] == 5:
            tc_lst[i] = 'FIV'
        if tc_lst[i] == 6:
            tc_lst[i] = 'SIX'
        if tc_lst[i] == 7:
            tc_lst[i] = 'SVN'
        if tc_lst[i] == 8:
            tc_lst[i] = 'EGT'
        if tc_lst[i] == 9:
            tc_lst[i] = 'NIN'

    print(tc)
    print(' '.join(tc_lst))
```

