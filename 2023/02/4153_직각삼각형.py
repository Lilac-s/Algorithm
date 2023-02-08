while 1:
    heru = list(map(int, input().split()))
    if heru[0] == 0 and heru[1] == 0 and heru[2] == 0:
        break
    else:
        heru.sort()
        if heru[2]*heru[2] == heru[0]*heru[0] + heru[1]*heru[1]:
            print('right')
        else:
            print('wrong')