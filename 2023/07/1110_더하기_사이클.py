def find_cycle(N):
    num = N       # 입력 값 저장 (변하는 값)
    count = 0     # 몇 번 사이클인지를 저장하는 변수

    while True:
        a = num // 10
        b = num % 10
        c = (a + b) % 10
        num = (b * 10) + c
        count += 1

        # 초기 입력값과 현재 값이 같으면 사이클 완료
        if num == N:
            break

    return count


if __name__ == "__main__":
    N = int(input())  # 정수를 입력받아서
    cycle_count = find_cycle(N)  # 함수를 호출하여 사이클 수를 계산하고
    print(cycle_count)  # 사이클 수를 출력합니다.
