import sys
lines = sys.stdin.readlines()
total = 0.0

i = 0
while i < len(lines):
	line = lines[i]
	details = line.split()
	mark = details[4]
	total += int(mark)
	i = i + 1

if total > 0:
	total = total / len(lines)
print total