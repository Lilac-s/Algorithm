# dp로 풀기
n = int(input())

# dp[i][0]: i자리 이친수 중 마지막 숫자가 0인 개수
# dp[i][1]: i자리 이친수 중 마지막 숫자가 1인 개수
dp = [[0] * 2 for _ in range(n+1)]
dp[1][1] = 1  # 첫 번째 자리는 1로 고정

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]  # i번째 자리가 0인 경우
    dp[i][1] = dp[i-1][0]  # i번째 자리가 1인 경우

result = dp[n][0] + dp[n][1]
print(result)


# 반복문으로 풀기
def count_pinary_numbers(n):
    if n <= 2:
        return 1

    count = 0
    prev_1 = 1
    prev_2 = 1

    for _ in range(3, n+1):
        count = prev_1 + prev_2
        prev_1, prev_2 = count, prev_1

    return count


n = int(input())
count = count_pinary_numbers(n)
print(count)


'''
def make_num(number, k):
    global cnt
    if k == n:
        if '11' not in number and number[0] != '0':
            cnt += 1
        return
    if k > n:
        return
    else:
        k += 1
        new_number = number + '0'
        make_num(new_number, k)
        if number[-1] == '0':
            number += '1'
            make_num(number, k)


n = int(input())
cnt = 0
num_lst = []
make_num('1', 1)
print(cnt)
'''
