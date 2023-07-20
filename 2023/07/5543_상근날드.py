prise = list(int(input()) for _ in range(5))
ham = min([prise[0], prise[1], prise[2]])
drink = min([prise[3], prise[4]])
print(ham+drink-50)
