import sys
p = sys.argv[1]
l = 0
i = 0
d = 0
s = 0


for c in p:
	if c.islower():
		l = 1
	elif c.isupper():
		i = 1
	elif c.isdigit():
		d = 1
	else:
		s = 1
total = l + i + d + s
print(total)