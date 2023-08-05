A, B, C = map(int, input().split())
X = B - A
Y = C - B
print(max(X, Y) - 1)
