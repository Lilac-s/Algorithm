def cross(s):
    Ai = stone_bridge[s]
    stone_bridge[s] = 0
    for i in range(-Ai, Ai+1, 1):
        if 0 <= s+i < N and stone_bridge[s+i] != 0:
            cross(s+i)
    return

N = int(input())
stone_bridge = list(map(int, input().split()))
S = int(input())

cross(S)
print(stone_bridge.count(0))