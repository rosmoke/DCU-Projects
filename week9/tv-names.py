import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	# dooo almost everything :)
	print " ".join(details[1:])
	i = i + 1