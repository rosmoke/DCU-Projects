import sys
s = sys.argv[1]
i = 0

while s[i].isspace():
	s = s[i+1:]
	print s
	i = i + 1
