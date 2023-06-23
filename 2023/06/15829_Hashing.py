L = int(input())
string = input()

r = 31  # 해시 함수에서 사용할 고유한 계수 r을 31으로 설정한다.
M = 1234567891  # 해시 함수에서 사용할 나누는 수 M을 1234567891으로 설정한다.

hash_value = 0  # 해시 값을 초기화한다.

# 문자열의 각 문자에 대해 반복한다.
for i in range(L):
    alpha_value = ord(string[i]) - ord('a') + 1
    # 현재 문자의 알파벳 순서를 구한다. (a: 1, b: 2, ..., z: 26)
    # ord(string[i]) - ord('a') + 1을 통해 알파벳 순서를 구한다.

    hash_value += alpha_value * (r ** i) % M
    # 알파벳 순서에 해당하는 값을 현재 위치의 고유한 계수 r의 거듭제곱과 곱하여 해시 값을 계산한다.
    # 해시 값은 이전까지의 해시 값에 현재 문자의 해시 값을 더하며 계산된다.

hash_value %= M  # 해시 값을 M으로 나눈 나머지를 구한다.

print(hash_value)  # 해시 값을 출력한다.
