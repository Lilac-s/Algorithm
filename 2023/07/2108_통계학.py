import sys
input = sys.stdin.readline

n = int(input())
summary = 0
numbers = list()
number_dict = dict()
max_num = -4001
min_num = 4001

for _ in range(n):
    number = int(input())
    summary += number
    numbers.append(number)
    if number in number_dict:
        number_dict[number] += 1
        
    else:
        number_dict[number] = 1
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

numbers.sort()

sorted_cnt_nums = sorted(number_dict.items(), key=lambda x: (-x[1], x[0]))
mode = sorted_cnt_nums[0][1]

lowest_lst = []
for num, cnt in sorted_cnt_nums:
    if cnt == mode:
        lowest_lst.append(num)
    else:
        break

lowest_lst.sort()

print(round(summary/n))
print(numbers[(n-1)//2])
if len(lowest_lst) > 1:
    print(lowest_lst[1])
else:
    print(lowest_lst[0])
print(max_num-min_num)
