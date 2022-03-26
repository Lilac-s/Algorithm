input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"

lst = list(map(int, input_str.split(', ')))

from collections import defaultdict
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]
    graph[a].append(b)
    graph[b].append(a)

queue = []
visited = []

queue.append(1)
visited.append(1)

from collections import deque

while queue:
    tmp = queue.pop(0)
    tmp = queue.popleft()

    for node in graph[tmp]:
        if node not in visited:
            queue.append(node)
            visited.append(node)
    print(queue)