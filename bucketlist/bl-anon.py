import sys
lines = sys.stdin.readlines()
i = 1
dictionary = {}

for line in lines:
	line = line.split(" ")
	if line[3] in dictionary:
		line[3] = dictionary[line[3]]
	else:
		dictionary[line[3]] = "user" + "-" + str(i)
		line[3] = dictionary[line[3]]
		i = i + 1
	sys.stdout.write(" ".join(line))