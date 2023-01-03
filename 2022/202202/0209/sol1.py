# n = int(input())

# 띄어쓰기로 구분된 여러 정수를 리스트로 받기
# lst = list(map(int, (input().split())))

# 띄어쓰기로 구분된 여러 정수를 리스트로 받기, 정수가 늘어날수록 변수 숫자도 늘어남.
# n, m = map(int, input().split())

# 띄어쓰기로 구분되지 않은 정수를 변수로 받기
# lst = list(map(int, input()))
# 이 경우에 split을 쓰면 하나로 모아져서 받아진다.

# 띄어쓰기로 구분된 문자 받기
# lst = input().split()

# 3차원 리스트가 입력될 때
# case1
# n = int(input())
# lst = [list(map(int, input().split())) for _ in range(n)]
#
# # case2
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))


#그리드 만들기
# 세로 m칸, 가로 n칸 grid 만들기 (여기서의)grid : 0으로 이루어진 2차원 리스트.
# n = 3
# m = 4

# lst = [[0]*3]*4
#
# lst2 = [[0]*3 for _ in range(4)]
#
# print(lst)
# lst[0][0] = 100
# print(lst)
#
# print(lst2)
# lst2[0][0] = 100
# print(lst2)

# 같은 위치에 있는 input.txt 파일을 테스트 케이스로 넣어준다.
import sys
sys.stdin= open('input.txt')