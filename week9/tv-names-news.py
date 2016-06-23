import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	name = " ".join(details)
	if name[12:21] == "BBC News ":
		print name
	i = i + 1
