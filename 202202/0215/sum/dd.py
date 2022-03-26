import sys
sys.stdin= open('sample_input(1).txt')

TC  = int(input())
num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)

#부분집합 구하기
lst = []
for i in range(1<<Len):
    sub_lst = []
    for j in range(Len):
        if i & (1<<j):
            sub_lst.append(num[j])
    lst.append(sub_lst)
print(lst)