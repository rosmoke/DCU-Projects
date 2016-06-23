import sys
word = sys.argv[1]

def chop(x):
	x = x[1:len(x)-1]
	return x

word = chop(word)
if len(word) > 0:
	print(word)
