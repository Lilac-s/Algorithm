while 1:
    name, age, weight = input().split(" ")
    if name == "#" and age == "0" and weight == "0":
        break
    elif int(age) > 17:
        print(name, "Senior")
        continue
    elif int(weight) >= 80:
        print(name, "Senior")
        continue
    else:
        print(name, "Junior")