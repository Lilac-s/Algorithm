import sys
sys.stdin= open('sample_input(1).txt')

T = int(input())
for tc in range(1, T+1):
    chars = input() # input 받기
    open_lst = ['(', '{']
    close = [')', '}'] # 여는 괄호와 닫는 괄호 분리
    stack = [] # 괄호를 받을 stack list 만들기

    for char in chars: # 인풋 받은 문자열을 순회하는 char
        if len(stack) == 0: # stack이 비어 있을 때
            if char in open_lst:
                stack.append(char) # 여는 괄호가 나오면 stack에 append 한다.
            elif char in close:
                stack.append(1)
                # break

        elif char == open_lst[0]:
            stack.append(char)
        elif char == open_lst[1]:
            stack.append(char) # 여는 괄호가 나올 때 stack에 append 한다.

        if char == close[0]:
            if stack[-1] == open_lst[0]:
                stack.pop()
            elif stack[-1] != open_lst[0]:
                stack.append(1)
            #     break
            # else:
            #     break

        if char == close[1]:
            if stack[-1] == open_lst[1]:
                stack.pop()
            elif stack[-1] == open_lst[1]:
                stack.append(1)
            #     break
            # else:
            #     break

    if len(stack) == 0:
        res = 1
    elif len(stack) != 0:
        res = 0

    print(f'#{tc} {res}')