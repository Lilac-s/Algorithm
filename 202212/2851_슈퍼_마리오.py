before = 0
after = 0
ans = 0

for _ in range(10):
    mush = int(input())
    after += mush
    if abs(after - 100) <= abs(before-100):
        ans = after
    before += mush
print(ans)