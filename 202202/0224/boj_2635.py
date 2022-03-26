A = int(input())

if A == 1:
    print(4)
    print('1 1 0 1')

else:
    mx_lst = []
    for B in range(1, A):
        C = A - B
        Ai_lst = [A, B, C]
        D = B - C

        while D>=0:
            D = Ai_lst[-2]-Ai_lst[-1]
            if D>=0:
                Ai_lst.append(D)
            else:
                break

        if len(Ai_lst) > len(mx_lst):
            mx_lst = Ai_lst

    print(len(mx_lst))
    print(*mx_lst)
