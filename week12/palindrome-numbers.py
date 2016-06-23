import sys
n = sys.argv[1]

def reverse(x):
	i = 0
	s = ""
	while i < len(x):
		s = s + n[len(x) - i - 1]
		i = i + 1
	return int(s)
	
i = 0
while int(n) != reverse(n) and i < 10:
	n = int(n) + reverse(n)
	n = str(n)
	i = i + 1
print n