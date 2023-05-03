a, b = map(int, input().split(" "))
a -= 1
b -= 1
a_row = a//4+1
b_row = b//4+1
a_col = a%4
b_col = b%4
print(abs(a_row-b_row)+abs(a_col-b_col))