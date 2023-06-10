for _ in range(int(input())):
    front, back = input().split("-")
    string_sum = 0
    for i in range(3):
        string_sum += (ord(front[i])-65)*26**(2-i)
    if abs(string_sum - int(back)) <= 100:
        print('nice')
    else:
        print('not nice')