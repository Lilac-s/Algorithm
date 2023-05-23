res_word = ""

def combine(a, b, c):
    global res_word
    word = a + b + c
    if res_word == "":
        res_word = word
    else:
        lst = [res_word, word]
        lst.sort()
        res_word = lst[0]

def flip(f, m, b):
    reverse_f = f[::-1]
    reverse_m = m[::-1]
    reverse_b = b[::-1]
    combine(reverse_f, reverse_m, reverse_b)

def divide(letter):
    for i in range(1, len(letter)-1):
        for j in range(i+1, len(letter)):
            front = letter[:i]
            middle = letter[i:j]
            back = letter[j:]
            flip(front, middle, back)

letter = input()
divide(letter)
print(res_word)