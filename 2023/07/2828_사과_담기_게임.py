screen_size, basket_size = map(int, input().split(" "))
j = int(input())
cnt = 0
now_left = 1
now_right = basket_size

for _ in range(j):
    apple = int(input())
    if now_left <= apple and apple <= now_right:
        continue
    if now_left > apple:
        move = now_left - apple
        cnt += move
        now_right -= move
        now_left = apple
    else:
        move = apple - now_right
        cnt += move
        now_left += move
        now_right = apple

print(cnt)
