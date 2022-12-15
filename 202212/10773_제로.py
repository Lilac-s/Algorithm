K = int(input())
integer_list = list()

for _ in range(K):
    integer = int(input())
    if integer == 0:
        integer_list.pop()
    else:
        integer_list.append(integer)

print(sum(integer_list))