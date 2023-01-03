numbers = list()
plus = 0

for _ in range(5):
    N = int(input())
    numbers.append(N)
    plus += N

numbers.sort()

print(plus//5)
print(numbers[2])