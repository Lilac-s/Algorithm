summary = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        summary += 40
    else:
        summary += score
print(int(summary/5))
