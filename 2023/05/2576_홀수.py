nums = list()
for _ in range(7):
    num = int(input())
    if num%2 == 1:
        nums.append(num)
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)