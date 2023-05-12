t = int(input())
for _ in range(t):
    space = input()
    n = int(input())
    candy = 0
    for _ in range(n):
        candy += int(input())
    if candy%n == 0:
        print("YES")
    else:
        print("NO")