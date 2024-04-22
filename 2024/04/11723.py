import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    tmp = list(input().split())
    oper = tmp[0]
    if oper == 'add':
        num = int(tmp[1])
        S.add(num)
    elif oper == 'remove':
        num = int(tmp[1])
        S.discard(num)
    elif oper == 'check':
        num = int(tmp[1])
        if num in S:
            print(1)
        else:
            print(0)
    elif oper == 'toggle':
        num = int(tmp[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif oper == 'all':
        S = set(range(1, 21))
    elif oper == 'empty':
        S.clear()