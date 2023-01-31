N = int(input())
papers = list(list(map(int, input().split())) for _ in range(N))
white = 0
blue = 0

def devision_paper(x, y, n):
    global white, blue
    is_same = papers[x][y]
    for i in range(n):
        for j in range(n):
            if is_same != papers[x+i][y+j]:
                devision_paper(x + n//2, y+ n//2, n//2)
                devision_paper(x+ n//2, y, n//2)
                devision_paper(x, y+ n//2, n//2)
                devision_paper(x, y, n//2)
                return
    if is_same == 0:
        white += 1
    else:
        blue += 1

devision_paper(0, 0, N)
print(white, blue)