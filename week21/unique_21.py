import sys
import string

words = [] # we remove punctuation and transform to lowercase
for line in sys.stdin:
	line = "".join(i for i in line if i not in string.punctuation)
	line = line.split()
	for word in line:
		words.append(word.lower())

i = len(words)-1
total = 0
while i >= 0:
	if words.pop() not in words:
		total = total + 1
	i = i - 1
print(total)