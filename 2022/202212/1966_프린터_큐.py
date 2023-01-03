T = int(input())

for _ in range(T):
    n, m = map(int, input().split(" "))
    queue = list(map(int, input().split(" ")))
    cnt = 0
    while queue:
        m -= 1
        if queue[0] < max(queue):
            delay = queue.pop(0)
            queue.append(delay)
            if m < 0:
                m = len(queue) -1
        elif queue[0] >= max(queue):
            queue.pop(0)
            cnt += 1
            if m < 0:
                print(cnt)
                break
            