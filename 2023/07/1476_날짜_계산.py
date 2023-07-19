E, S, M = map(int, input().split())  # 입력값 E, S, M을 받음
year = 1  # 시작 연도를 1로 초기화

while True:
    if ((year - E) % 15 == 0) and ((year - S) % 28 == 0) and ((year - M) % 19 == 0):
        break  # E, S, M과의 차이가 각각 15, 28, 19의 배수인 경우 반복문 종료
    year += 1  # 연도를 1씩 증가시킴

print(year)  # 결과 연도 출력
