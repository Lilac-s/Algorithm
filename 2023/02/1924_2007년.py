x, y = map(int, input().split())
cnt = 0
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
daycounts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0, x-1):
    cnt += daycounts[i]
cnt += y
print(days[cnt%7])