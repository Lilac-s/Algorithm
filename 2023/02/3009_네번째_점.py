x_lst = list()
y_lst = list()

for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

x_res = 0
y_res = 0

for i in x_lst:
    if x_lst.count(i) == 1:
        x_res = i

for i in y_lst:
    if y_lst.count(i) == 1:
        y_res = i

print(x_res, y_res)