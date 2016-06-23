import sys
arguments = len(sys.argv)
t = 1
word = []
while t < arguments:
	line = sys.argv[t]
	word.append(line)
	t = t + 1
words = {
	"one": "eins",
	"two": "zwei",
	"three": "drei",
	"four": "vier",
	"five": "funf",
	"six": "sechs",
	"seven": "sieben",
	"eight": "acht",
	"nine": "neun",
	"ten": "zehn"
}

i = 0
while i < len(word):
	if word[i] in words:
		word[i] = words[word[i]]
	i = i + 1
print " ".join(word)