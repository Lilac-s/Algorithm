firstNum, secondNum = input().split(" ")
flipFirstNum = int(firstNum[::-1])
flipSecondNum = int(secondNum[::-1])

print(max([flipFirstNum, flipSecondNum]))

