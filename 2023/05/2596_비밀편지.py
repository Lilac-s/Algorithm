letter_lst = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
letter_res = ["A", "B", "C", "D", "E", "F", "G", "H"]
n = int(input())
numbers = input()
answer = ""
status = True
for i in range(n):
    letter = numbers[i*6:(i+1)*6]
    res_let = 0
    diff_cnt = 6
    for k in range(8):
        let = letter_lst[k]
        cnt = 0
        for j in range(6):
            if let[j] != letter[j]:
                cnt += 1
        if cnt <= diff_cnt:
            diff_cnt = cnt
            res_let = letter_res[k]
    if diff_cnt >= 2:
        status = False
        print(i+1)
        break
    else:
        answer += res_let
if status == True:
    print(answer)
