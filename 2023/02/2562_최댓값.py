mx_number = 0
mx_index = 0

for i in range(1, 10):
    num = int(input())
    if num > mx_number:
        mx_number = num
        mx_index = i

print(mx_number)
print(mx_index)