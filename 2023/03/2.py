lst = list(input())[1:-1]
print(lst)
i = 0
res = 0
while 1:
    if lst[i] == "<":
        i += 1
        res += 1
    else:
        break

j = len(lst)-1
while 1:
    if lst[j] == ">":
        j -= 1
        res += 1
    else:
        break
print(res)