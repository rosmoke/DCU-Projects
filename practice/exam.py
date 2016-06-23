
lines = sys.stdin.readlines() # second mistake

i = 0
longest_line = lines[0] # third mistake
while i < len(lines): # first mistake
	if len(longest_line) < len(lines[i]):
		longest_line = lines[i] # fourth mistake
	i = i + 1
print longest_line