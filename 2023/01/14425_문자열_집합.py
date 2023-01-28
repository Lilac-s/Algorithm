N, M = map(int, input().split())
gather = []
words = []
cnt = 0

for i in range(N):
    gather.append(input())

for j in range(M):
    words.append(input())

for k in range(len(words)):
    if words[k] in gather:
        cnt += 1

print(cnt)