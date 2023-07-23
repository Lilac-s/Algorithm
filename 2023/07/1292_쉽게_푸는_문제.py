numbers = list()
n = 1
while n <= 1000:
    for _ in range(n):
        numbers.append(n)
    n += 1
a, b = map(int, input().split(" "))
print(sum(numbers[a-1:b]))
