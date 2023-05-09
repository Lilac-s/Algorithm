number = input()
status = False
if len(number) == 1:
    print("NO")
else:
    for i in range(1, len(number)):
        front = 1
        back = 1
        for j in number[i:]:
            front*=int(j)
        for j in number[:i]:
            back*=int(j)
        if front == back:
            status = True
    if status == True:
        print("YES")
    else:
        print("NO")