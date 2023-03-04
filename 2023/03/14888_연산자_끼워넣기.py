import sys

def dfs(idx, cal):
    global min_res, max_res
    if idx == n-1:
        min_res = min(min_res, cal)
        max_res = max(max_res, cal)
        return
    else:
        for i in range(4):
            if oper_kind[i]:
                oper_kind[i] -= 1
                if i == 0:
                    dfs(idx+1, cal + numbers[idx+1])
                if i == 1:
                    dfs(idx+1, cal - numbers[idx+1])
                if i == 2:
                    dfs(idx+1, cal * numbers[idx+1])
                if i == 3:
                    if cal < 0 and numbers[idx+1] > 0:
                        pos_cal = abs(cal)
                        dfs(idx+1, -(pos_cal // numbers[idx+1]))
                    else:
                        dfs(idx+1, cal // numbers[idx+1])
                oper_kind[i] += 1


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
visited = list(False for _ in range(n-1))
oper_kind = list(map(int, sys.stdin.readline().rstrip().split()))
min_res = 1e9
max_res = -1e94

dfs(0, numbers[0])

print(max_res)
print(min_res)