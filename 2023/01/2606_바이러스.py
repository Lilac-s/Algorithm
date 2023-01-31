N = int(input())
computer_number = int(input())
graph = list([]*N for _ in range(N+1))
visited = [0]*(N+1)

for _ in range(computer_number):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)

# for _ in range(computer_number):
#     x, y = map(int, input().split())
#     connect[x-1][y-1] = 1
#     connect[y-1][x-1] = 1

# cnt = 0
# def dfs(x, y):
#     global cnt
#     for i in range(N):
#         if y != 0 and connect[y][i] == 1:
#             connect[y][i] = 0
#             cnt += 1
#             dfs(y, i)
        

# for i in range(N):
#     if connect[0][i] == 1:
#         connect[0][i] = 0
#         dfs(0, i)

# print(cnt//2)