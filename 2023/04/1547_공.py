m = int(input())
cups = [1, 0, 0]
for i in range(m):
    x, y = map(int, input().split(" "))
    if cups[x-1] == 1:
        cups[x-1] = 0
        cups[y-1] = 1
    elif cups[y-1] == 1:
        cups[y-1] = 0
        cups[x-1] = 1
print(cups.index(1)+1)