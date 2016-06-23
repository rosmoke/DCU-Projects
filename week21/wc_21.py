import sys
total = 0
for word in sys.stdin:
	word = word.split()
	total = total + len(word)
print(total)