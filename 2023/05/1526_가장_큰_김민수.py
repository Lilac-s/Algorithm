number = int(input())
while 1:
    status = True
    for i in str(number):
        if i != '4' and i != '7':
            status = False
            number -= 1
    if status:
        print(number)
        break