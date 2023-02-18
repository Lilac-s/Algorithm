word = list(input())
alphabet ='abcdefghijklmnopqrstuvwxyz'
ans = []

for i in range(len(alphabet)):
    if alphabet[i] not in word:
        ans.append('-1')
    elif alphabet[i] in word:
        ans.append(str(word.index(alphabet[i])))

print(" ".join(ans))