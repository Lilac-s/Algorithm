score = list(int(input()) for _ in range(8))
num = ['1', '2', '3', '4', '5', '6', '7', '8']

for i in range(7, 0, -1):
    for j in range(i):
        if score[j] > score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]
            num[j], num[j + 1] = num[j + 1], num[j]

print(sum(score[3:]))
print(' '.join(sorted(num[3:])))
