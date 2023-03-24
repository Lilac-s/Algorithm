N = int(input())
A_lst = list(map(int, input().split(" ")))
A_lst.sort()
M = int(input())
numbers = list(map(int, input().split(" ")))
for i in numbers:
    front, back = 0, N-1
    isExist = False
    while front <= back:
        mid = (front+back)//2
        if i == A_lst[mid]:
            isExist = True
            print(1)
            break
        elif i > A_lst[mid]:
            front = mid+1
        else:
            back = mid-1
    if not isExist:
        print(0)