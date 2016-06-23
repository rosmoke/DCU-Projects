import sys

l = ["OF", "TO", "IN", "IT", "IS", "BE", "AS", "AT", "SO", "WE", "HE", "BY", "OR", "ON", "DO", "IF", "ME", "MY", "UP", "AN", "GO", "NO", "US", "AM"]

a = []
b = []
words = []
x = []
para = []

for line in sys.stdin:
    details = line.split()
    a.append(details)

for n in a:
    for word in n:
        if len(word) == 2 and word != "--":
            x.append(word)

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

i = 0
while i < 36:
    for n in x:
        encoded_txt = ''
        for char in n:
            try:
                temp_char = alphabet.index(char) + i
                encoded_txt += alphabet[temp_char]
            except ValueError:
                encoded_txt += char
            except IndexError:
                temp_char = (alphabet.index(char) - (36 - i))
                encoded_txt += alphabet[temp_char]
        if encoded_txt in l:
            words.append(encoded_txt)

    if len(words) == len(x):
        break

    words = []
    i = i + 1

j = i

i = 0
while i < len(a):
    for c in a[i]:
        encoded_txt = ''
        for char in c:
            try:
                temp_char = alphabet.index(char) + j
                encoded_txt += alphabet[temp_char]
            except ValueError:
                encoded_txt += char
            except IndexError:
                temp_char = (alphabet.index(char) - (36 - j))
                encoded_txt += alphabet[temp_char]
        b.append(encoded_txt)

    para.append(" ".join(b))
    b = []
    i = i + 1

for v in para:
    sys.stdout.write(v)
    sys.stdout.write("\n")
