times = int(input())

# 나이가 가장 많은 사람
mx_n, mx_d, mx_m, mx_y = "", 31, 12, 2010
# 나이가 가장 적은 사람
mn_n, mn_d, mn_m, mn_y = "", 1, 1, 1990

for _ in range(times):
    name, day, month, year = input().split(" ")
    day = int(day)
    month = int(month)
    year = int(year)

    if year < mx_y:
        mx_n, mx_d, mx_m, mx_y = name, day, month, year
    if year == mx_y and month < mx_m:
        mx_n, mx_d, mx_m, mx_y = name, day, month, year
    if year == mx_y and month == mx_m and day < mx_d:
        mx_n, mx_d, mx_m, mx_y = name, day, month, year
    
    if year > mn_y:
        mn_n, mn_d, mn_m, mn_y = name, day, month, year
    if year == mn_y and month > mn_m:
        mn_n, mn_d, mn_m, mn_y = name, day, month, year
    if year == mn_y and month == mn_m and day > mn_d:
        mn_n, mn_d, mn_m, mn_y = name, day, month, year

print(mn_n, mx_n)

"""
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990
"""