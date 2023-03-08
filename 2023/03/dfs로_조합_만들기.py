m = 2
arr = [1, 2, 3]
comb_lst = []

def dfs(host_lst, pick_lst, idx):
    if idx == len(arr):
        if len(pick_lst) == m:
            comb_lst.append(pick_lst[:])
        return
    else:
        pick_lst.append(host_lst[idx])
        dfs(host_lst, pick_lst, idx+1)
        pick_lst.pop()
        dfs(host_lst, pick_lst, idx+1)

dfs(arr, [], 0)
print(comb_lst)













