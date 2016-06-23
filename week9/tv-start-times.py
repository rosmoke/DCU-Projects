import sys
lines = sys.stdin.readlines()
i = 0

while i < len(lines):
	line = lines[i]
	details = line.split()
	line = " ".join(details)
	start_time = line[:5]
	name = line[12:]
	print start_time + " " + name
	i = i + 1