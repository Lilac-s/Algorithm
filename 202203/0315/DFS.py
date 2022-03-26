input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"

lst = list(map(int, input_str.split(', ')))

from collections import defaultdict
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]
    graph[a].append(b)
    graph[b].append(a)

stack = []
visited = []

stack.append(1)
visited.append(1)
cnt = 0

while stack:
    cnt += 1
    tmp = stack[-1]
    for node in graph[tmp]:
        if node not in visited:
            stack.append(node)
            visited.append(node)
            break
    else:
        stack.pop()