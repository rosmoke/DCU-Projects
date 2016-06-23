s = raw_input()
i = 0
letter = len(s)
word = ""

while i <= len(s):
	word += s[letter:letter + 1]
	i = i + 1
	letter = letter - 1
print word