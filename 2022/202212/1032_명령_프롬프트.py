N = int(input())
original = []

for _ in range(N):
    if original == []:
        original = list(input())
    else:
        new = list(input())
        for i in range(len(new)):
            if original[i] != new[i]:
                original[i] = "?"

print("".join(original))