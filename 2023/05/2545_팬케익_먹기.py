t = int(input())

for _ in range(t):
    input()  # 빈 줄을 입력받아서 무시한다.
    a, b, c, d = map(int, input().rstrip().split(" "))
    # A, B, C를 오름차순으로 정렬한다.
    a, b, c = sorted((a, b, c))
    
    # 팬케익을 자르고 남은 변의 총 길이를 계산한다.
    total_length = a + b + c - d
    # 첫 번째 변의 길이를 계산한다. (최대값은 팬케익의 가로 길이 a이거나 총 길이의 1/3이다.)
    first_side = min(total_length // 3, a)
    # 사용된 첫 번째 변의 길이를 총 길이에서 뺀다.
    total_length -= first_side
    # 두 번째 변의 길이를 계산한다. (최대값은 팬케익의 세로 길이 b이거나 남은 총 길이의 1/2이다.)
    second_side = min(total_length // 2, b)

    # 최종적으로 남은 부피를 계산하여 출력한다.
    print(first_side * second_side * (total_length - second_side))
