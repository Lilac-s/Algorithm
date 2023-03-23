from collections import deque

n = int(input())
for i in range(n):
    ps = deque(input())
    check = list()
    while ps:
        v = ps.popleft()
        if v == "(":
            check.append(v)
        else:
            if len(check) <= 0:
                check.append("!")
                break
            else:
                check.pop()
    if len(ps) == 0 and len(check) == 0:
        print("YES")
    else:
        print("NO")