# melon = int(input())
# len_lst = [list(map(int, input().split())) for _ in range(6)]
#
# print(len_lst)
#
# dir_lst = []
#
# for i in range(6):
#     a = len_lst[i][0]
#     dir_lst.append(a)
#     if dir_lst.count(i) == 1:
#
#
#
# print(dir_lst)

# melon = int(input())
# len_lst1 = [list(map(int, input().split())) for _ in range(6)]
# len_lst2 = len_lst1*3
# # print(len_lst2)
#
# nb_lst = []
# ds_lst = []
#
# for i in range(6, 12, 1):
#     if len_lst2[i][0] == 3 or len_lst2[i][0] == 4:
#         nb_lst.append(len_lst2[i])
#     elif len_lst2[i][0] == 1 or len_lst2[i][0] == 2:
#         ds_lst.append(len_lst2[i])
#
# nb = 0
# nb_s = 0
# ds = 0
# ds_s = 0
#
# for j in range(6, 12, 1):
#     if len_lst2[j][1] == max(nb_lst[0][1], nb_lst[1][1], nb_lst[2][1]):
#         nb = len_lst2[j][1]
#         nb_s = abs(len_lst2[j-1][1] - len_lst2[j+1][1])
#     elif len_lst2[j][1] == max(ds_lst[0][1], ds_lst[1][1], ds_lst[2][1]):
#         ds = len_lst2[j][1]
#         ds_s = abs(len_lst2[j - 1][1] - len_lst2[j + 1][1])
#
# print((nb*ds - nb_s*ds_s)*melon)

# melon = int(input())
# len_lst1 = [list(map(int, input().split())) for _ in range(6)]
# len_lst2 = len_lst1*3
# # print(len_lst2)
#
# nb_lst = []
# ds_lst = []
#
# for i in range(6, 12, 1):
#     if len_lst2[i][0] == 3 or len_lst2[i][0] == 4:
#         nb_lst.append(len_lst2[i])
#     elif len_lst2[i][0] == 1 or len_lst2[i][0] == 2:
#         ds_lst.append(len_lst2[i])
#
# nb = 0
# nb_s = 0
# ds = 0
# ds_s = 0
#
# for j in range(6, 12, 1):
#     if len_lst2[j][1] == max(nb_lst[0][1], nb_lst[1][1], nb_lst[2][1]):
#         nb = len_lst2[j][1]
#     elif len_lst2[j][1] == max(ds_lst[0][1], ds_lst[1][1], ds_lst[2][1]):
#         ds = len_lst2[j][1]
#
#
# print((nb*ds - nb_s*ds_s)*melon)

k = int(input())

max_length = []
small_length = []

a = [list(map(int, input().split())) for _ in range(6)]
a_idx = [i[0] for i in a]

for i in a_idx:
    if a_idx.count(i) == 1:
        max_length.append(a[a_idx.index(i)][1])
        if a_idx.index(i) == 5:
            small_length.append(abs(a[a_idx.index(i)-1][1] - a[a_idx.index(i)-5][1]))
        else:
            small_length.append(abs(a[a_idx.index(i)-1][1] - a[a_idx.index(i)+1][1]))

small_area = small_length[0] * small_length[1]
max_area = max_length[0] * max_length[1]

print(k * (max_area - small_area))