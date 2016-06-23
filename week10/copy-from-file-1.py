import sys
text = open("translation.txt")

for line in text.readlines():
	sys.stdout.write(line)