a, b = input().split()  # 두 개의 문자열을 입력받음

answer = []  # 각 위치에서의 다른 문자 개수를 저장할 리스트

# b 문자열을 순회하면서 a 문자열과 비교하여 다른 문자 개수를 세고 저장
for i in range(len(b) - len(a) + 1):
    count = 0  # 다른 문자 개수를 세는 변수
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1  # 다른 문자가 나올 때마다 count 증가
    answer.append(count)  # 현재 위치에서의 다른 문자 개수를 answer 리스트에 추가

print(min(answer))  # answer 리스트의 최솟값 출력
