import sys

J = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
jersey = []
size_dict = {'S': 0, 'M': 1, 'L': 2}
cnt = 0

for j in range(J):
    jersey.append([j+1, size_dict[sys.stdin.readline().rstrip()]])

for i in range(A):
    size, number = sys.stdin.readline().rstrip().split()
    if jersey[int(number)-1][1] >= size_dict[size]:
        jersey[int(number)-1][1] = -1
        cnt += 1

print(cnt)