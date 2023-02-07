while 1:
    number = input()
    if number == '0':
        break
    else:
        reverse_number = number[::-1]
        if reverse_number == number:
            print('yes')
        else:
            print('no')