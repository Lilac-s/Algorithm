T = int(input())

for _ in range(T):
    r, s = input().split()
    word = ''
    cnt = 0
    while len(word) < int(r)*len(s):
        for i in range(int(r)):
            word += s[cnt]
        cnt += 1
    print(word)