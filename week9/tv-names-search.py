import sys
a = " ".join(sys.argv[1:]) + " "
lines = sys.stdin.readlines()
i = 0

while i < len(lines):
	line = lines[i]
	details = line.split()
	name = " ".join(details)
	if name[12:21] == a:
		print name
	i = i + 1
