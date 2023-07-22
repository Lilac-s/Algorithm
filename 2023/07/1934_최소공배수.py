def gcd(x, y):  # 최대공약수 구하기
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):  # 최소공배수 구하기
    result = (x * y) // gcd(x, y)
    return result


num = int(input())  # 테스트 케이스의 개수를 입력 받음

for i in range(num):  # 테스트 케이스의 개수만큼 반복
    x, y = map(int, input().split())  # 두 개의 정수 x, y를 입력 받음
    print(lcm(x, y))  # 최소공배수를 계산하여 출력
