import sys
s = sys.argv[1]
i = 0

while i < len(s):
	if i != len(s)-1 and s[i] == s[i+1]:
		s = s[:i] + s[i] + s[i+2:]
	else:
		i = i + 1
print s