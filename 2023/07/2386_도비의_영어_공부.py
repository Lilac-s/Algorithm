while True:
    letters = list(input())
    if letters[0] == '#':
        break
    cnt = letters.count(letters[0]) + letters.count(letters[0].upper()) - 1
    print(letters[0], cnt)
