from collections import deque
cards = deque()
n = int(input())
for i in range(1, n+1):
    cards.append(i)

while 1:
    if len(cards) <= 1:
        break
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards[0])