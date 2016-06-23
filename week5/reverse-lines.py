lines = []
line = raw_input()
while line != "end":
	lines.append(line)
	line = raw_input()
while 0 < len(lines):
	print lines.pop()