paper = [list("0"*100) for _ in range(100)]
cnt = int(input())

for i in range(cnt):
    x, y = map(int, input().split(" "))
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = "1"

count = 0
for k in range(100):
    count += paper[k].count("1")

print(count)