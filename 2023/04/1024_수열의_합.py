n, l = map(int, input().split(" "))
for i in range(l, 101):
    num = n - (i*(i+1)/2)
    if num%i == 0:
        num = int(num/i)
        if num >= -1:
            for j in range(1, i+1):
                print(num+j, end=" ")
            print()
            break
else:
    print(-1)