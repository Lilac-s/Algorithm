import sys
sys.stdin= open('sample_input(2).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int,input().split())))
    truck = sorted(list(map(int, input().split())))
    go_weight = 0

    while truck and container:
        truck_weight = truck.pop()
        container_weight = container.pop()
        if truck_weight < container_weight:
            truck.append(truck_weight)
        if truck_weight >= container_weight:
            go_weight += container_weight

    print(f'#{tc} {go_weight}')