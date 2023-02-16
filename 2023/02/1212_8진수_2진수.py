number = '0o' + input()
new_number = int(number, 8)
print(bin(new_number)[2:])