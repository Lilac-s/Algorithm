n, l = map(int, input().split(" "))
label = n
num = 0
while label > 0:
    num += 1
    if str(l) in str(num):
        continue
    label -= 1
print(num)