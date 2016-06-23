import sys #2
lines = sys.readlines()
longest_line = ""

i = 0
while i < len(lines): #1
	if len(longest_line) < len(lines[i]):
		longest_line = line[i]
	i = i + 1
print longest_line