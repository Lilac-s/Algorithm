letters = list(input())
change_letters = {
    'B' : 'v',
    'E' : 'ye',
    'H' : 'n',
    'P' : 'r',
    'C' : 's',
    'Y' : 'u',
    'X' : 'h',
    'A' : 'a',
    'K' : 'k',
    'M' : 'm',
    'O' : 'o',
    'T' : 't'
}
alphabets = list()

for i in range(len(letters)):
    alphabets.append(change_letters[letters[i]])

print("".join(alphabets))