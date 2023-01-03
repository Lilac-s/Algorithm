lights = input()

# 값을 변화시키기 위해 list로 만들기
# 편리한 인덱싱(배수계산)을 위해 앞에 N 붙여주기
n = len(lights)
lights = list("N" + lights)


cnt = 0
for i in range(1, n+1):
    # 스위치를 누르는 과정
    # 켜져있는 아이를 꺼야해
    if lights[i] == "Y": # 만일 켜져있으면
        cnt += 1

        for j in range(i, n+1):
            if j % i == 0:
                if lights[j] == "N":
                    lights[j] == "Y"
                elif lights[j] == "Y":
                    lights[j] == "N"
print(cnt)

# 답이 안 나와