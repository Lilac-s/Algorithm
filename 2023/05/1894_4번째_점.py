numbers = list(map(float, input().split(" ")))
numbers.sort()
set(numbers)
row = numbers[2] - numbers[0]
column = numbers[3] - numbers[1]
row += numbers[4]
column += numbers[5]
x = row - numbers[0]
