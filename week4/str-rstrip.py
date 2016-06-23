import sys
s = sys.argv[1]
i = len(s)-1

while s[i].isspace():
	s = s[0:i]
	i = i - 1
print s, "-", len(s)