import sys

s = sys.argv[1]
i = 0

while i < len(s):
	if s[i].islower():
		s = s[:i] + "x" + s[i+1:]
		i = i + 1
	elif s[i].isupper():
		s = s[:i] + "X" + s[i+1:]
		i = i + 1
	else:
		i = i + 1
print s