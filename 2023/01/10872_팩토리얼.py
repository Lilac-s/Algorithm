N = int(input())

def pac(n, res):
    if n == 1:
        print(res)
    elif n == 0:
        print(1)
    else:
        n = n-1
        res = res*n
        pac(n, res)

pac(N, N)