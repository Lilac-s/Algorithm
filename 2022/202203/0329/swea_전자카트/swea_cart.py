import sys
sys.stdin= open('sample_input(1).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
