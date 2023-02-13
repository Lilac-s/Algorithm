def switch(status):
    if status == 1:
        return 0
    else:
        return 1

number_of_switch = int(input())
switches = [0] + list(map(int, input().split()))
number_of_students = int(input())
for i in range(number_of_students):
    # 1 = boy, 2 = girl
    gender, received_number = map(int, input().split())
    if gender == 1:
        cnt = 1
        while received_number * cnt <= number_of_switch:
            switches[received_number * cnt] = switch(switches[received_number * cnt])
            cnt += 1
    else:
        cnt = 1
        switches[received_number] = switch(switches[received_number])
        while received_number + cnt <= number_of_switch and received_number - cnt > 0:
            up_new_number = received_number + cnt
            down_new_number = received_number - cnt
            if switches[up_new_number] == switches[down_new_number]:
                switches[up_new_number] = switch(switches[up_new_number])
                switches[down_new_number] = switch(switches[down_new_number])
                cnt += 1
            else:
                break
for j in range(1, len(switches)):
    print(switches[j], end=" ")
print()