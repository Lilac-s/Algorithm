T = int(input())
for tc in range(1, T+1):
    N = int(input())
    K, A, B = map(int, input().split())
    busstop = [0]*1001
    for _ in range(N):
