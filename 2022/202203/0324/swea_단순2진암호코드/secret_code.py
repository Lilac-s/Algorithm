import sys
sys.stdin= open('input (1).txt')

def find(code):
    odd_num = 0
    even_num = 0
    gum = 0
    for i in range(0, len(code), 7):
        imsi = code[i:i+7]
        code2 = 0
        if imsi == '0001101':
            code2 = 0
        if imsi == '0011001':
            code2 = 1
        if imsi == '0010011':
            code2 = 2
        if imsi == '0111101':
            code2 = 3
        if imsi == '0100011':
            code2 = 4
        if imsi == '0110001':
            code2 = 5
        if imsi == '0101111':
            code2 = 6
        if imsi == '0111011':
            code2 = 7
        if imsi == '0110111':
            code2 = 8
        if imsi == '0001011':
            code2 = 9
        if i % 2 == 0 or i == 0:
            odd_num += code2
        if i % 2 == 1 and i != len(code):
            even_num += code2
        if i == len(code):
            gum += code2
    if (odd_num*3 + even_num + gum) % 10 == 0:
        return odd_num + even_num + gum
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code_lst = []
    for _ in range(N):
        code_all = input()
        x = 0
        for i in range(len(code_all)-1, 0, -1):
            if code_all[i] == '1':
                x = i
                break
        code = code_all[x-55:x+1]
        if code != '':
            code_lst.append(find(code))

    print(f'#{tc} {code_lst[0]}')

    # res = 0
    # for _ in range(N):
    #     code = input()
    #     odd_num = 0
    #     even_num = 0
    #     gum = 0
        # for i in range(0, len(code), 7):
        #     tmp = code[i:i+7]
        #     imsi = 0
        #     if tmp == '0001101':
        #         imsi = 0
        #     if tmp == '0011001':
        #         imsi = 1
        #     if tmp == '0010011':
        #         imsi = 2
        #     if tmp == '0111101':
        #         imsi = 3
        #     if tmp == '0100011':
        #         imsi = 4
        #     if tmp == '0110001':
        #         imsi = 5
        #     if tmp == '0101111':
        #         imsi = 6
        #     if tmp == '0111011':
        #         imsi = 7
        #     if tmp == '0110111':
        #         imsi = 8
        #     if tmp == '0001011':
        #         imsi = 9
        #     print(tmp)
        #     print(imsi)
        #     if i % 2 == 0:
        #         odd_num += imsi
        #     if i % 2 == 1 and i != 7:
        #         even_num += imsi
        #     else:
        #         gum += imsi
        # if odd_num*3 + even_num + gum % 10 == 0:
        #     res += odd_num*3 + even_num + gum
        # print(res)
