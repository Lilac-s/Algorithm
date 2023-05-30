t = int(input())

for _ in range(t):
    status = True
    dots = list()
    for _ in range(4):
        x, y = map(int, input().split(" "))
        dots.append([x, y])
    lengths = list()
    for i in range(4):
        for j in range(i+1, 4):
            first_dot = dots[i]
            second_dot = dots[j]
            length = (first_dot[0] - second_dot[0])**2 + (first_dot[1] - second_dot[1])**2
            lengths.append(length)
    lengths.sort()
    side_len = lengths[:4]
    diag_len = lengths[4:]
    if side_len.count(side_len[0]) != 4:
        status = False
    if diag_len.count(diag_len[0]) != 2:
        status = False
    if status:
        print(1)
    else:
        print(0)