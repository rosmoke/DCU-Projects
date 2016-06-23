import sys
import operator
d = {}

def vowels(c):
	if c == "a" or c == "e" or c == "o" or c == "i" or c == "u":
		return True
for line in sys.stdin:
	words = line[:-2].lower().replace("."," ").replace(","," ").split()
	for word in words:
		for c in word:
			if c in d:
				d[c] += 1
			elif c.isalpha() and vowels(c):
				d[c] = 1

for key, value in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
		print(("{} : {:>3}").format(key, value))