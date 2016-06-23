import sys

lines = sys.stdin.readlines()
i = 1
info = {}


for data in lines:
	data = data.split(" ")
	if data[3] in info:
		data[3] = info[data[3]]
	else:
		info[data[3]] = "user-" + str(i)
		data[3] = info[data[3]]
		i = i + 1
	print data