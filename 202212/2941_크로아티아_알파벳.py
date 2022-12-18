alphabet = list(input())
replace = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in range(len(alphabet)-1):
    if i+2 < len(alphabet) and alphabet[i] + alphabet[i+1] + alphabet[i+2] in replace:
        alphabet[i] = ' '
        alphabet[i+1] = ' '
        alphabet[i+2] = ' '
        cnt += 1
    elif alphabet[i] + alphabet[i+1] in replace:
        alphabet[i] = ' '
        alphabet[i+1] = ' '
        cnt += 1

while ' ' in alphabet:
    alphabet.remove(' ')

cnt += len(alphabet)
print(cnt)