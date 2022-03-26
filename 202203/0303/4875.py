
def srch(lst, x, y, arrive):
    global is_arrive
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 가고자 하는 곳
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < len(lst) and 0 <= b < len(lst) and not arrive[a][b]:
            # 인덱스 에러를 막기 위함
            # 방문한 곳인지 아닌지 확인 (false)
            arrive[a][b] = True
            if lst[a][b] == 3: # 목적지 : True로 바꿔준다.
                is_arrive = True
            elif lst[a][b] == 0:
                srch(lst, a, b, arrive) # 재귀

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)] # 미로 input
    # 확인한 곳을 true로 바꾸기 위해 false로 체크리스트 만들기
    can_lst = [[False for _ in range(N)] for i in range(N)]
    is_arrive = False # 기본값을 false로 두고 목적지에 도달하면 true로 바꿔준다.
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: # 2를 먼저 찾는다
                srch(maze, i, j, can_lst) # 2의 위치에서 함수 시작
    if is_arrive:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

# is_arrive를 사용하지 않아도 ok