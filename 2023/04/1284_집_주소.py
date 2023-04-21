while 1:
    num = input()
    if num == '0':
        break
    res = 1
    for i in num:
        if i == '1':
            res += 3
        elif i == '0':
            res += 5
        else:
            res += 4
    print(res)