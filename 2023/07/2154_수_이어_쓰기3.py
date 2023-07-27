n = int(input())
new_number = ''
num = 1
while num <= n:
    new_number += str(num)
    num += 1
print(new_number.find(str(n))+1)
