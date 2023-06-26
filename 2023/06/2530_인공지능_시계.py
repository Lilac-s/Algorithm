# 현재 시각 입력
current_hour, current_minute, current_second = map(int, input().split(" "))

# 오븐구이에 필요한 시간 입력
cooking_time = int(input())

# 오븐구이가 끝나는 시각 계산
current_second += cooking_time
current_minute += current_second//60
current_hour += current_minute//60

# 결과 출력
print(current_hour%24, current_minute%60, current_second%60)