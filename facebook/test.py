lines = []
line = raw_input()

while line != "end":
	n = ""
	i = 0
	while i <= len(line):
		n = line[i] + n
		i += 1
	lines.append(n)

	line = raw_input()
print lines
#j = 0
#while j < len(lines):
#	print lines[j]
#	j += 1