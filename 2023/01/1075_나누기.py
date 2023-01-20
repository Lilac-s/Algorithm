N = int(input())
F = int(input())
multiple = (N//100*100) // F

if multiple * F >= N//100*100:
    res = multiple * F
else:
    res = multiple * F + F

if len(str(res)) > 1:
    print(str(res)[-2:])
else:
    print(f'0{str(res)}')


# N = int(input())
# F = int(input())
# multiple = 0
# i = 1

# while multiple < N//100*100:
#     multiple = i * F
#     i += 1
# print(multiple)

# if len(str(multiple)) > 1:
#     print(str(multiple)[-2:])
# else:
#     print(f'0{str(multiple)}')