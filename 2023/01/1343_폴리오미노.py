board = list(input())
replace = []

for i in range(len(board)):
    if board[i] == 'X':
        replace.append('X')
    if board[i] == '.':
        if len(replace) % 2 == 0:
            for j in range(len(replace)):
                if len(replace) % 4 == 0:
                    board[i-j-1] = 'A'
                else:
                    board[i-j-1] = 'B'
                    replace.pop(0)
            replace = []
        else:
            print(-1)
            break
    if i == len(board)-1:
        if len(replace) % 2 == 0:
            for j in range(len(replace)):
                if len(replace) % 4 == 0:
                    board[i-j] = 'A'
                else:
                    board[i-j] = 'B'
                    replace.remove('X')
            print(''.join(board))
        else:
            print(-1)