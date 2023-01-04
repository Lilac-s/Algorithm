N = int(input()) # N = 분해합
generator = 0

for i in range(1, N+1):
    digits = list(map(int, str(i)))
    generator = i + sum(digits)
    if generator == N:
        print(i)
        break
    if i == N:
        print(0)


