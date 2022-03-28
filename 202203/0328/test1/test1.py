dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상 하 좌 우

def dfs(rabbit, go, dis, i): # 토끼가 이동하면서 농장을 돌아다니는 함수
    x = rabbit[0]
    y = rabbit[1] # 주어진 위치에 토끼를 위치시킨다.
    farm[x][y] = i # 농장에 토끼가 있는 곳을 i로 바꾼다.
    nx = x + dis*dx[go]
    ny = y + dis*dy[go] # 문제에 주어진 방향에 맞춰서 토끼를 이동거리만큼 이동시킨다.
    # 만일 토끼가 농장 안에 있고 그곳이 아직 가지 않은 곳이라면
    if 0 <= nx < N and 0 <= ny < N and farm[nx][ny] != i:
        rabbit[0] = nx
        rabbit[1] = ny # 토끼를 새로운 위치로 이동시킨다.
        dfs(rabbit, go, dis, i) # 다시 dfs 함수를 돌린다.
    else: # 토끼가 농장을 벗어났다면
        return # 종료한다.

T = int(input()) # 테스트케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    farm = list([0]*N for _ in range(N)) # visited 역할을 해줄 fram

    for i in range(M):
        *rabbit, go, dis = map(int, input().split())
        dfs(rabbit, go, dis, i+1) # 토끼 정보에 맞춰서 input을 받아 함수에 넣는다.

    cnt = 0
    for i in range(N):
        for j in range(N):
            if farm[i][j] != 0:
                cnt += 1 # farm이 0이 아니라면 당근을 훔쳐갔으므로 수를 세준다.

    print(f'#{tc} {cnt}') #출력문