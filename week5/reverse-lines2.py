lines = []
line = ""
while line != "end":
	line = raw_input()
	lines.append(line)
while 0 < len(lines):
	print lines.pop()