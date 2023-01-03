dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] # 시계 방향 (우 하 좌 상)
# dx dy는 k번, k-1번, k-1번, k-1번 움직이며 물고기를 잡는다.

def fish(x, y):
    cnt = 0 # 물고기 수를 세기 위한 cnt
    cnt += water_fish[x][y] # 첫 번째 물고기를 더해준다.
    for a in range(1, K): # 오른쪽으로
        nx = x + dx[0]*a
        ny = y + dy[0]*a
        cnt += water_fish[nx][ny]

    for b in range(1, K): # 아래로
        nnx = nx + dx[1]*b
        nny = ny + dy[1]*b # 원래 자리 nx ny를 고정시킨 채로 이동
        cnt += water_fish[nnx][nny]

    for c in range(1, K): # 왼쪽으로
        n_x = nnx + dx[2]*c
        n_y = nny + dy[2]*c
        cnt += water_fish[n_x][n_y]

    for d in range(1, K-1): # 위로
        n__x = n_x + dx[3]*d
        n__y = n_y + dy[3]*d
        cnt += water_fish[n__x][n__y]
    return cnt # 물고기를 다 더한 cnt를 리턴해준다.


T = int(input())
for tc in range(1, T+1): # 테스트케이스만큼 돌기
    N, M, K = map(int, input().split())
    water_fish = [list(map(int, input().split())) for _ in range(N)]
    # 인풋 받기 (K가 그물 크기)

    res = 0
    for i in range(N):
        for j in range(M): # x y 좌표를 순회한다.
            if 0 <= i+K-1 < N and 0 <= j+K-1 < M: # 인덱스 에러 방지
                tmp = fish(i, j)
                if res < tmp:
                    res = tmp # 가장 큰 값을 구하기 위한 로직
    print(f'#{tc} {res}') # 출력문