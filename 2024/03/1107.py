n = int(input())
m = int(input())
cnt = abs(100-n)
if m > 0:
    broken_buttons = list(map(int, input().split(' ')))
    for num in range(500000*2+1):
        num = str(num)
        for j in range(len(num)):
            if int(num[j]) in broken_buttons:
                break
            elif j == len(num)-1:
                cnt = min(cnt, abs(int(num)-n)+len(num))
    print(cnt)
else:
    print(min(cnt, len(str(n))))