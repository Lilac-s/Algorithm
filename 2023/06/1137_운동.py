n, m, M, T, R = map(int, input().split(" "))
time = 0
exersize_time = 0
pulse = m
if m + T > M:
    print(-1)
else:
    while time < n:
        if pulse + T <= M:
            pulse += T
            time += 1
            exersize_time += 1
        else:
            pulse -= R
            if pulse < m:
                pulse = m
            exersize_time += 1
    print(exersize_time)