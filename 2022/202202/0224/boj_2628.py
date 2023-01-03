R, C = map(int, input().split())
line = int(input())
col_cut = []
row_cut = []

for i in range(line):
    A, B = map(int, input().split())
    if A == 0:
        col_cut.append(B)
    elif A == 1:
        row_cut.append(B)

col_cut.append(C)
row_cut.append(R)

col_cut.sort()
row_cut.sort()
# print(col_cut)
# print(row_cut)

mx_col = 0
mx_row = 0

for c in range(1, len(col_cut)):
    col = col_cut[c] - col_cut[c-1]
    if mx_col <= col:
        mx_col = col

for r in range(1, len(row_cut)):
    row = row_cut[r] - row_cut[r-1]
    if mx_row <= row:
        mx_row = row

print(mx_row*mx_col)
