N = int(input())
M = int(input())
room = [0] # 건물 앞의 벽 (1번 방의 왼쪽 벽)
for r in range(1, N+1):
    room.append(7)
    room.append(0) # 방을 7로 표시하고, 방의 벽을 0으로 표시한다.

# 예를 들어 방이 5개 있다면,
# room = [0, 7, 0, 7, 0, 7, 0, 7, 0, 7] 이다.

for m in range(M):
    x, y = map(int, input().split())
    for i in range(y-x):
        room[x*2 + i*2] = -1 # 종빈이에 의해 무너진 벽을 -1로 표현해 준다.

# 예를 들어 종빈이가 1, 3으로 움직였다면,
# room = [0, 7, -1, 7, -1, 7, 0, 7, 0, 7] 이다.

for j in range(len(room)-1):
    if room[j] == -1: # 만일 벽이 -1으로 무너져 있다면,
        room[j] = 0 # 벽을 다시 0으로 만들어 주고,
        room[j+1] = 0 # 방이 통합되어 버렸으므로 방도 0으로 만들어 준다.

# 이 방식을 지나고 나면
# room = [0, 7, 0, 0, 0, 0, 0, 7, 0, 7] 이 된다.
# 따라서 맨 앞의 방만 남는다.

res = room.count(7) # 7의 개수를 세어주면 남은 방 개수를 구할 수 있다.
print(res)