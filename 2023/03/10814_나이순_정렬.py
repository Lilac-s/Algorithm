import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split(" ")
    people.append((int(age), name))
people.sort(key=lambda age:age[0])
for i in range(len(people)):
    print(people[i][0], people[i][1])
