import sys
s = sys.argv[1]
i = 0

while s[i].isspace(): # checking leading spaces and remove them
	s = s[i+1:]
	i = i + 1

i = len(s)-1
while s[i].isspace(): # checking trailing spaces and remove them
	s = s[0:i]
	i = i - 1
print s, "-", len(s)