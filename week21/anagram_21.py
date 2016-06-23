import sys

for line in sys.stdin:
	line = line.split()
	f = "".join(sorted(list(line[0])))
	s = "".join(sorted(list(line[1])))
	print(f == s)