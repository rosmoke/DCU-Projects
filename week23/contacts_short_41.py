import sys
f = open(sys.argv[1])
d = {}

for line in f:
	contact = line.split()
	d[contact[0]] = contact[1]

for name in sys.stdin:
	if name[:-1] in d:
		print("Phone:", d[name[:-1]])
	else:
		print("No such contact")