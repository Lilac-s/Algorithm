def Rev(number):
    reverse_number = number[::-1]
    # try:
    #     int(reverse_number)
    # except:
    #     reverse_number = reverse_number.lstrip('0')
    return int(reverse_number)


x, y = map(str, input().split(' '))
rev_num = Rev(x) + Rev(y)
print(Rev(str(rev_num)))
