from collections import deque
n = int(input())
cards = deque([])
result = list()

for num in range(1, n+1):
    cards.append(num)

while len(cards) > 1:
    throw_out = cards.popleft()
    result.append(str(throw_out))
    if len(cards) > 1:
        top_card = cards.popleft()
        cards.append(top_card)

result.append(str(cards[0]))
print(" ".join(result))