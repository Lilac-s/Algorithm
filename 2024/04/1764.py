import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
heardlooked = {}
result = []
for _ in range(n):
    heard = input().strip()
    heardlooked[heard] = True
for _ in range(m):
    looked = input().strip()
    value = heardlooked.get(looked)
    if value == None:
        continue
    else:
        result.append(looked)

result.sort()
print(len(result))
for res in result:
    print(res)