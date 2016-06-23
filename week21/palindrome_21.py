import sys
line = sys.argv[1:]
phrase = []
for word in line:
	word = word.lower()
	word = list(word)
	for c in word:
		if c.isalpha():
			phrase.append(c)
print(phrase == phrase[::-1])

