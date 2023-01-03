N = int(input())
body = list(list(map(int, input().split(" "))) for _ in range(N))
rank_list = list()

for i in range(N):
    rank = 1
    x, y = body[i][0], body[i][1]
    for j in range(N):
        if j != i:
            z, w = body[j][0], body[j][1]
            if x < z and y < w:
                rank += 1
    rank_list.append(str(rank))

print(" ".join(rank_list))