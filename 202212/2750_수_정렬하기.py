N = int(input())
numbers = list(int(input()) for _ in range(N))
numbers.sort()
for i in range(N):
    print(numbers[i])