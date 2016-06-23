s = raw_input()
i = 0
t = ""

while i < len(s):
	if i % 2 == 0:
		t += s[i]
		i = i + 1
	else:
		i = i + 1
print t