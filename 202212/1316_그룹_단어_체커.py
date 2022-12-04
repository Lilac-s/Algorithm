N = int(input())
cnt = N

for _ in range(N):
    word = list(input())
    alpha = []
    for i in range(len(word)):
        if word[i] in alpha and word[i-1] != word[i]:
            cnt -= 1
            break
        if word[i] not in alpha:
            alpha.append(word[i])

print(cnt)