import sys
evil = ['e', 'v', 'i', 'l']

lines = sys.stdin.readlines()
for line in lines:
	line = line.rsplit()
	check = ""
	for c in line[0].lower():
		if c in evil:
			check += c
	if check == 'evil':
		print(line[0])