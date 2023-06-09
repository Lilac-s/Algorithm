while True:
    number = input()
    if number == '0':
        break
    else:
        status = True
        while status:
            if len(number) == 1:
                status = False
            else:
                summary = 0
                for num in number:
                    summary += int(num)
                number = str(summary)
        print(number)