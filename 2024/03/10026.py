import sys
sys.setrecursionlimit(10**6)

def make_a_zone(x, y, color):
    global visited
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and picture[nx][ny] == color and visited[nx][ny] == True:
            visited[nx][ny] = False
            make_a_zone(nx, ny, color)

def red_green_zone(x, y, color):
    global red_green_visited
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if color == 'B':
            if 0 <= nx < n and 0 <= ny < n and picture[nx][ny] == 'B' and red_green_visited[nx][ny] == True:
                red_green_visited[nx][ny] = False
                red_green_zone(nx, ny, color)
        else:
            if 0 <= nx < n and 0 <= ny < n and picture[nx][ny] != 'B' and red_green_visited[nx][ny] == True:
                red_green_visited[nx][ny] = False
                red_green_zone(nx, ny, color)

n = int(input())
picture = list(list(sys.stdin.readline().strip()) for _ in range(n))
visited = list([True]*n for _ in range(n))
red_green_visited = list([True]*n for _ in range(n))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
red_green_cnt = 0

for x in range(n):
    for y in range(n):
        if visited[x][y] == True:
            cnt += 1
            visited[x][y] = False
            make_a_zone(x, y, picture[x][y])
        if red_green_visited[x][y] == True:
            red_green_cnt += 1
            red_green_visited[x][y] = False
            red_green_zone(x, y, picture[x][y])

print(cnt, red_green_cnt)
