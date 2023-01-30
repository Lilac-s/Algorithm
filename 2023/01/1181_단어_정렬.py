import sys

N = int(sys.stdin.readline())
word_lst = list()

for i in range(N):
    word_lst.append(sys.stdin.readline().strip())

set_word = set(word_lst)
res = list(set_word)
res.sort()
res.sort(key=len)

for j in range(len(res)):
    print(res[j])


# for _ in range(N):
#     word = input()
#     if len(word_lst) == 0:
#         word_lst.append(word)
#     else:
#         for i in range(len(word_lst)):
#             if len(word_lst[i]) > len(word) and word not in word_lst:
#                 word_lst.insert(i, word)
#                 break
#             if len(word_lst[i]) == len(word) and word not in word_lst:
#                 if word_lst[i] > word:
#                     word_lst.insert(i, word)
#                     break
#             if i == len(word_lst)-1 and word not in word_lst:
#                 word_lst.append(word)
#                 break

# for j in range(len(word_lst)):
#     print(word_lst[j])

# N = int(input())
# lst = list(input() for _ in range(N))

# for rotate in range(N-1):
#     i = 0
#     for j in range(i, N-rotate):
#         if len(lst[i]) > len(lst[j]):
#             lst[i] = 0
#         i += 1
# print(lst)