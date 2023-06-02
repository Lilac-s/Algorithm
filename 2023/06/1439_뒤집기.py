import sys
input = sys.stdin.readline

s = input()
cnt_zero = 0
cnt_one = 0
status = 'initial'
for i in s:
    if status == 'initial':
        if i == '1':
            status = True
            cnt_one += 1
        elif i == '0':
            status = False
            cnt_zero += 1
    elif i == '1' and status == False:
        cnt_one += 1
        status = True
    elif i == '0' and status == True:
        cnt_zero += 1
        status = False
print(min(cnt_zero, cnt_one))