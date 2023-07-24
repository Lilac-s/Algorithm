'''
# 뒤뒤뒤, 뒤뒤앞, 뒤앞뒤, 뒤앞앞, 앞뒤뒤, 앞뒤앞, 앞앞뒤, 앞앞앞
coin_case = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
p = int(input())
for _ in range(p):
    cnt_case = [0, 0, 0, 0, 0, 0, 0, 0]
    throw_result = input()
    for i in range(38):
        sequence = throw_result[i:i+3]
        for j in range(8):
            if coin_case[j] == sequence:
                cnt_case[j] += 1
    print(' '.join(map(str, cnt_case)))
'''


def count_coin_sequences(throw_result):
    coin_case = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
    cnt_case = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(throw_result) - 2):
        sequence = throw_result[i:i+3]
        for j in range(8):
            if coin_case[j] == sequence:
                cnt_case[j] += 1

    return cnt_case


p = int(input())  # 테스트 케이스의 개수를 입력 받음

for _ in range(p):
    throw_result = input()  # 동전 던진 결과 입력 받음
    result = count_coin_sequences(throw_result)  # 동전 던진 결과로 각 경우의 개수를 계산
    print(' '.join(map(str, result)))  # 각 경우의 개수를 출력
