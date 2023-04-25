scores = list()

for i in range(5):
    score = list(map(int, input().split(" ")))
    scores.append(sum(score))

winner_score = max(scores)
print(scores.index(winner_score)+1, winner_score)