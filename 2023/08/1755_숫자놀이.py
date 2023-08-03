# 숫자를 영문으로 변환하는 딕셔너리
num_to_str_dict = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'
}

# 범위 시작과 끝을 입력받는다.
start, end = map(int, input().split())

# 숫자와 그에 해당하는 영문을 저장하는 리스트를 생성한다.
number_and_str_list = []
for number in range(start, end + 1):
    # 숫자를 문자열로 변환하고 각 자리수를 영문으로 바꾼 뒤, 리스트에 추가한다.
    str_number = ' '.join([num_to_str_dict[char] for char in str(number)])
    number_and_str_list.append([number, str_number])

# 영문 기준으로 정렬한다.
number_and_str_list.sort(key=lambda x: x[1])

# 숫자를 출력한다. 한 줄에 10개씩 출력한다.
for idx, (number, _) in enumerate(number_and_str_list):
    if idx % 10 == 0 and idx != 0:
        print()
    print(number, end=' ')
