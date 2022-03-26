std = int(input())

a = std // 2
b = std % 2
if b == 1:
    c = std * a
elif b == 0:
    c = std * (a - 1) + a
print(c)