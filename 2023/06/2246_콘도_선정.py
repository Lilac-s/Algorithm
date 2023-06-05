n = int(input())
condominiums = list()
for _ in range(n):
    d, c = map(int, input().split())
    condominiums.append((d, c))
condominiums.sort()
max_charge = 10001
cnt = 0
for condo in condominiums:
    charge = condo[1]
    if charge < max_charge:
        max_charge = charge
        cnt += 1
print(cnt)