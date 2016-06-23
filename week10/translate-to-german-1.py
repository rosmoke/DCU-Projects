import sys
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

word = sys.argv[1]

print "The German for", word, "is", words[word]+"."