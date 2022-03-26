from collections import deque
my_chu = 20
next_person = 1

q = deque()
q.append([1,1])

while 1:
    num, cnt = q.popleft()
    my_chu -= cnt
    q.append([num,cnt +1])
    q.append([next_person +1, 1])
    print(q)

    if my_chu <= 0:
        break
