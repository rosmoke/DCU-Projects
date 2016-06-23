counts = []
v = raw_input()
presence = False
while v != "end":
	presence = False
	if len(counts) == 0:
		counts.append(v)
		v = raw_input()
	for i in range(len(counts)):
		if counts[i][0] == v:
			counts[i] = counts[i] + "*"
			if counts[i][1] == "*":
				counts[i] = counts[i][0]+" **"
			presence = True
	if presence is not True:
		counts.append(v)
	v = raw_input()
n = 0
while n < 10:
	for i in counts:
		if n == int(i[0]):
			print i
	n = n + 1