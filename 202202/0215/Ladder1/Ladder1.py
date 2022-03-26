import sys
sys.stdin= open('input.txt')

for tc in range(10): # 테스트케이스 10개
    tc = int(input()) # 테스트케이스 인풋 받기

    lst = [list(map(int, input().split())) for _ in range(100)] # 그리드 형태로 ladder 인풋 받기

    for i in range(100): # 도착 지점 찾기
        # 도착 지점은 가장 아래에 있으므로 lst[-1]을 먼저 쓰고,
        # i가 for문을 돌면서 2로 표현된 도착 지점을 찾는다.
        if lst[-1][i] == 2:
            y = i # 도착 지점을 y로 설정한다.
            break

    x = 99 # x는 99, y는 i부터 시작해서 올라가면서 탐색한다.

    dx = [0, 0, -1] # x는 위로 올라가기만 할 것이다.
    dy = [1, -1, 0] # y는 양쪽을 보면서 확인하면서 올라갈 것이다.

    while x != 0: # x가 0이 되면 가장 위로 올라간 것이므로, x가 0이 아닐 때 계속 작동하는 while문을 설정한다.

        for d in range(3): # 방향 3개를 확인하는 for문 (왼쪽, 오른쪽, 위쪽!)
            nx = x + dx[d] # 내가 갈 수 있는 후보 위치를 새로 설정하기.
            ny = y + dy[d]
            # 인덱스 에러가 발생하지 않게 0<=nx<100 and 0<=ny<100 를 설정한다.
            # x는 조건을 설정하지 않아도 인덱스 에러가 발생하지 않는다. while문으로 설정해 두었기 때문.
            # lst[nx][ny] == 1는 사다리인걸 확인하는 문장이다.
            if 0<=nx<100 and 0<=ny<100 and lst[nx][ny] == 1:
                # 지금 내가 있는 곳을 0으로 설정하여 계속 반복하며 왔다갔다 하지 않게 한다(좌우좌우...).
                    lst[x][y] = 0
                    x = nx
                    y = ny # 새롭게 할당하며 이동
    print(f'#{tc} {y}')