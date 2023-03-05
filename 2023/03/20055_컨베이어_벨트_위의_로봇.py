import sys
from collections import deque

# "내리는 위치에 도달하면 그 즉시 내린다"를 잘 해석해야 했다.
# 문제를 꼼꼼히 확인하자.
def step_one():
    # 밸트의 회전
    kan = belt.pop()
    belt.appendleft(kan)
    robot.pop()
    robot.appendleft(False)
    if robot[n-1] == True:
        robot[n-1] = False

def step_two():
    # 로봇의 이동 (내구도 감소)
    for i in range(n-1, -1, -1):
        if robot[i] and i == n-1 and belt[i]:
            robot[i] = False
            belt[i] -= 1
        if robot[i] and i < n-1 and belt[i+1] and not robot[i+1]:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1

def step_three():
    # 로봇 올리기 (내구도 감소)
    if belt[0] != 0 and not robot[0]:
        belt[0] -= 1
        robot[0] = True

def step_four():
    # 내구도가 0인 칸이 K개 이상이라면 종료
    cnt = 0
    for i in range(len(belt)):
        if belt[i] <= 0:
            cnt += 1
    if cnt >= k:
        return False
    else:
        return True

n, k = map(int, sys.stdin.readline().rstrip().split())
belt = deque(map(int, sys.stdin.readline().rstrip().split()))
robot = deque(False for _ in range(n))
step_cnt = 0
status = True
while status:
    step_cnt += 1
    step_one()
    step_two()
    step_three()
    status = step_four()
print(step_cnt)