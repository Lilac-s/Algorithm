n = int(input())
numbers = list(int(input()) for _ in range(n))


def check_arithmetic(numbers):
    diff = numbers[1] - numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i+1] - numbers[i] != diff:
            return False
    return True


def check_geometric(numbers):
    ratio = numbers[1] // numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i+1] // numbers[i] != ratio:
            return False
    return True


if check_arithmetic(numbers):
    print(numbers[-1] + (numbers[1] - numbers[0]))
elif check_geometric(numbers):
    print(numbers[-1] * (numbers[1] // numbers[0]))

'''
n = int(input())
numbers = list(int(input()) for _ in range(n))
grade = numbers[1] - numbers[0]
ratio = numbers[1]//numbers[0]
status = 0
for i in range(1, n-1):
    if numbers[i+1] - numbers[i] == grade:
        status = 'grade'
    if numbers[i+1]//numbers[i] == ratio:
        status = 'ratio'
    else:
        break
if status == 'grade':
    print(numbers[-1]+grade)
elif status == 'ratio':
    print(numbers[-1]*ratio)
'''
