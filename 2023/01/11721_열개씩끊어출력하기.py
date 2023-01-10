lst = list(input())

for i in range(len(lst)//10+1):
    print("".join(lst[i*10:i*10+10]))