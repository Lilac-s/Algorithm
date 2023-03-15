res = 0
numbers = list(map(int, input().split(" ")))
for i in range(5):
    res += numbers[i]*numbers[i]
print(res%10)