while 1:
    letters = input()
    store = list()
    if letters == "." :
        break
    for i in letters:
        if i == '(' or i == '[':
            store.append(i)
        elif i == ')':
            if len(store) != 0 and store[-1] == '(':
                store.pop()
            else:
                store.append(')')
                break
        elif i == ']':
            if len(store) != 0 and store[-1] == '[':
                store.pop()
            else:
                store.append(']')
                break
    if len(store) == 0:
        print("yes")
    else:
        print("no")