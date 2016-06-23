import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	mark = details[4]
	print mark
	i = i + 1