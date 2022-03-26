# N = int(input())
# # arr = [list(map(int, input().split())) for _ in range(N)]
# # print(arr)
#
# arr1 = [0] + list(map(int, input().split())) + [0]
# print(arr1)
# arr2 = [[0]*(N+2) + [[0]+list(map(int, input().split())) + [0] for _ in range(N)] + [0]*(N+2)]
# print(arr2)

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# for k in range(4):
#     ni = i +di[k]
#     nj = j + dj[k]
#     if 0<=ni<N and 0<=nj<M:
#         arr[ni][nj]

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = 3
# for i in range(N):
#     for j in range(N):
#         for di, dj in[(0,1), (1,0), (0,1), (-1,0)]:
#             ni = i + di
#             nj = j + dj
#             if 0<=ni<N and 0<=nj<N:
#                 print(i, j, arr[ni][nj])
#         print()

# def BubbleSort(a, N) : # 정렬할 List, N 원소 수
#     for i in range(N-1, 0, -1): # 범위의 끝 위치
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)