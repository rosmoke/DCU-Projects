import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	if i == 0:
		tmp = details
	elif int(details[4]) > int(tmp[4]):
		tmp = details
	i = i + 1
if len(lines) > 0:
	print " ".join(tmp[5:])