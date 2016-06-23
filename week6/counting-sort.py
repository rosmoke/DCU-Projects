count = []
for i in range(1000):
	count.append(0)
v = raw_input()
while v != "end":
	count[int(v)] = count[int(v)] + 1
	v = raw_input()
i = 0
for c in count:
	if c >= 1:
		for b in range(c):
			print i
	i = i + 1