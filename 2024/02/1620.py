import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
book = {}
book_lst = [0]*(n+1)

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    book[name] = i
    book_lst[i] = name

for i in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(book_lst[int(question)])
    else:
        print(book[question])