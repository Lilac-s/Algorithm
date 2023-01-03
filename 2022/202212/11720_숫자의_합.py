N = int(input())

number = list(input())
cnt = 0
for i in range(len(number)):
    cnt += int(number[i])

print(cnt)
