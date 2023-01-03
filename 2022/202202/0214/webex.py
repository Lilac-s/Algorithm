
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
for i in range(3):
    # print(lst[i])
    for j in lst[i]:
        print(j, end=" ")
    print() # 키패드 모양 꺼내기

for j in range(3):
    for i in range(3):
        # print(lst[i][j]) # 세로로 값 꺼내기
        print(lst[i][j], end=" ")
    print() # 세로로 바뀐 키패드 모양 꺼내기

for i in range(3):
    for j in range(3):
        print(lst[j][i]) # 이렇게 행과 열에 i와 j를 거꾸로 해도 상관은 없지만 앞으로 익숙해지기 좋게 일관성을 주자
# 교수님은 편한 대로 하라고 하셨음


# 역순(대각선 오른쪽 위에서 왼쪽 아래로)인덱스는 어떻게 접근해야 할까?
for i in range(3):
    print(lst[i][-i-1])


# 지그재그 순회
for i in range(4):
    if i%2 == 0:
        for j in range(4):
            print(lst[i][j])
        pass
    elif i%2 == 1:
        for j in range(4):
            print(lst[i][-j-1])
        for j in range(3, -1, -1):
            print(lst[i][j])
        pass
        #아니 똑같은데 왜 나는 오류가 생기지?
        


# 전치 행렬
lst[x+1][y]
lst[x][y+1]
lst[x-1][y]
lst[x][y-1] # 이걸 반복하고 싶지 않아서 만든 거야


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
[1, -1, 0, 0]
[0, 0, 1, -1]
[1, 1, 1, 0, 0, -1, -1, -1]
[0, -1, 1, 1, -1, 0, 1, -1] # 8방향 모두 돌아볼 수 있다.
# 행렬을 사용하고 있는 거지 수평선 수직선을 사용하는 게 아니야

x, y = 0, 0
for d in range(4):
    nx = x + di[d]
    ny = y + dj[d]
    #이 아래에서 nx, ny를 가지고 논다(?)

for i in range(3):
    for j in range(3):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 일정 위치를 기준으로 상하좌우를 반복하게 된다.

            if 0 <= nx < n and 0 <= ny < n:
                # 작업을 무엇인가 할거야!

            if nx < 0 or nx>=n or ny<=0 or :
                # 작업 안해!
                

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(3):
    for j in range(3):
        lst[i][j]

for j in range(3):
    for i in range(3):
        lst[i][j]

for i in range(3):
    for j in range(3):
        lst[j][i]

grid = [[0]*3 for _ in range(3)]

for j in range(3):
    for i in range(3):
        grid[j][i] = lst[i][j]
'''

zip, map

lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

lst = list(map(list, zip(*lst)))
for i in lst:
    print(i)

lst = list(map(list, zip(*lst[::-1])))
for i in lst:
    print(i)