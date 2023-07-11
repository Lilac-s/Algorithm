n, kjm, ihs = map(int, input().split(" "))
cnt = 0
while True:
    cnt += 1
    if kjm % 2 == 0:
        kjm = kjm//2
    else:
        kjm = kjm//2 + 1
    if ihs % 2 == 0:
        ihs = ihs//2
    else:
        ihs = ihs//2 + 1
    if kjm == ihs:
        break
print(cnt)
