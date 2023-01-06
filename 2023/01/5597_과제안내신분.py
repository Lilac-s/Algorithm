numbers = []
for i in range(1, 31):
    numbers.append(i)

for j in range(28):
    number = int(input())
    numbers.remove(number)

for k in range(len(numbers)):
    print(numbers[k])