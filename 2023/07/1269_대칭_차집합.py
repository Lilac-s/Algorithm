a, b = map(int, input().split(" "))
first_lst = list(map(int, input().split(" ")))
second_lst = list(map(int, input().split(" ")))

# 겹치는 숫자들의 개수를 구함
intersection = len(set(first_lst) & set(second_lst))

# 결과 출력
result = a + b - 2 * intersection
print(result)


'''from collections import deque

a, b = map(int, input().split(" "))
first_lst = list(map(int, input().split(" ")))
second_lst = list(map(int, input().split(" ")))
first_lst.sort()
second_lst.sort()
first = deque(first_lst)
second = deque(second_lst)

cnt = 0
i = 0

while i < len(first) and i < len(second):
    while first[i] != second[i]:
        if first[i] > second[i]:
            second.popleft()
            cnt += 1
        else:
            first.popleft()
            cnt += 1
    i += 1

print(len(first) + len(second) - cnt)
'''
