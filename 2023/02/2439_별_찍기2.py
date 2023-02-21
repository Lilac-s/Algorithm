N = int(input())
lst = list(" " for _ in range(N))
for i in range(1, N+1):
    lst[-i] = '*'
    print("".join(lst))