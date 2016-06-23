import sys
d = {}
for line in sys.stdin:
	tokens = line[:-2].lower().replace("."," ").split()
	for token in tokens:
		if token in d:
			d[token] += 1
		else:
			d[token] = 1
for key, value in sorted(d.items()):
	print(key, ":",value)