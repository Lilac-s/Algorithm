n = int(input())
for i in range(n):
    if i == 0:
        print(n*"*")
    else:
        print((i-1)*" ",(n-i)*"*")