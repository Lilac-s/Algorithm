import sys
sys.stdin= open('sample_input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     iron = list(input())
#     len_iron = len(iron)
#     cnt = 0
#     sol = 0
#     i = 0
#
#     while i<len_iron:
#         if iron[i] == '(':
#             cnt +=1
#             i +=1
#         elif iron[i] == ')' and iron[i-1] == '(':
#             cnt -=1
#             sol += cnt
#             i +=1
#         elif iron[i] == ')':
#             cnt -=1
#             sol +=1
#             i +=1
#         else:
#             break
#     print(f'#{tc} {sol}')

t = int(input())
for _ in range(1, t+1):
    a = input()

    temp = 0
    result = 0
    for i in range(len(a)-1):
        if a[i] == '(' and a[i+1] == ')':
            result += temp
        elif a[i] == ')' and a[i+1] == '(':
            pass
        elif a[i] == '(' and a[i+1] == '(':
            temp += 1
            result += 1
        elif a[i] == ')' and a[i+1] == ')':
            temp -= 1
    print(f'#{_} {result}')
