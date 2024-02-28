n, m, b = map(int, input().split(' '))
ground = list(list(map(int, input().split(' '))) for _ in range(n))

min_time = 1e9
max_height = 0

for target_height in range(257):
    remove_block = 0
    add_block = 0

    for i in range(n):
        for j in range(m):
            if ground[i][j] > target_height:
                remove_block += ground[i][j] - target_height
            else:
                add_block += target_height - ground[i][j]
    
    if remove_block + b - add_block >= 0:
        time = remove_block*2 + add_block
        if time <= min_time:
            max_height = target_height
            min_time = time

print(min_time, max_height)
