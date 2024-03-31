from collections import deque

t = int(input())
for _ in range(t):
    p = list(input())
    n = int(input())
    if n == 0:
        empty = input()
        if 'D' in p:
            print('error')
        else:
            print(empty)
    else:
        queue = deque(list(map(int, input()[1:-1].split(','))))
        status = True
        r_cnt = 0
        for func in p:
            if func == 'R':
                r_cnt += 1
            elif func == 'D':
                try:
                    if r_cnt % 2 == 1:
                        queue.pop()
                    else:
                        queue.popleft()
                except:
                    print('error')
                    status = False
                    break
        if status:
            if r_cnt % 2 == 1:
                queue.reverse()
            print(f"[{','.join(map(str, queue))}]")

'''
시간 초과가 발생할 걸 알면서도 뒤집는 방법으로 풀었다가,
reverse를 쓰지 않아도 풀 수 있다는 걸 알고 나서 해결했다.
가능하다면 리스트를 변경하기보다는 순회하는 방식으로 풀고,
시간 복잡도에 문제가 있다고 예상되는 방식은
구현 전에 5분이라도 더 고민해 보는 습관을 들여야겠다.
'''