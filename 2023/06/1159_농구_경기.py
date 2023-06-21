import sys
input = sys.stdin.readline

n = int(input())
surnames = dict()
for _ in range(n):
    name = input()
    if name[0] not in surnames.keys():
        surnames[name[0]] = 1
    else:
        surnames[name[0]] += 1
        
res = []
for key in surnames.keys():
    if surnames[key] >= 5:
        res.append(key)

if len(res) > 0:
    res.sort()
    print(''.join(res))
else:
    print("PREDAJA")