before = 0
after = 0
answer = 0

for _ in range(10):
    mush = int(input())
    after += mush
    if abs(after - 100) <= abs(before-100):
        answer = after
    before += mush
print(answer)