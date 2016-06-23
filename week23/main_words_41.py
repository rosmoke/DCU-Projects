import sys
d = {}
for line in sys.stdin:
	tokens = line[:-2].lower().replace("."," ").replace(","," ").split()
	for token in tokens:
		if token in d:
			d[token] += 1
		elif len(token) > 3:
			d[token] = 1
for key, value in sorted(d.items()):
	if value > 2:
		print(key, ":",value)