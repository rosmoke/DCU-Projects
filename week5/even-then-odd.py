odd = []
even = []
x = []
while x != "end":
	x = raw_input()
	if x != "end" and int(x) % 2 == 0:
		odd.append(int(x))
	elif x != "end" and int(x) % 2 != 0:
		even.append(int(x))
for x in odd:
	print x
for x in even:
	print x