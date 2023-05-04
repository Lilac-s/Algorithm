p, k = map(int, input().split(" "))
status = True
for i in range(2, k):
    if p%i == 0:
        print("BAD", i)
        status = False
        break
if status == True:
    print("GOOD")