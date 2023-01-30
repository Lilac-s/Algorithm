name = list(input())
count = dict()

for i in range(len(name)):
    if name[i] in list(count.keys()):
        count[name[i]] += 1
    else:
        count[name[i]] = 1

word_lst = sorted(count.keys())
odd_word = ""
for word in word_lst:
    if count.get(word) % 2 == 1:
        if odd_word == "":
            odd_word = word
        else:
            print("I'm Sorry Hansoo")
            exit(0)

res = ""
temp = ""
for word in word_lst:
    number = count.get(word) // 2
    temp += word*number
    count[word] = int(count[word] / 2)
res += temp
if odd_word != "":
    res += odd_word
res += temp[::-1]

print(res)