lst = list(map(int, input().split()))
lst.sort()
a = lst[0] + lst[3]
b = lst[1] + lst[2]
print(abs(a-b))