import sys
f = sys.argv[1]
try:
	t = open(f, 'r')
	text = t.readlines()
	high_mark = 0
	high_name = ""
	more = 0
	for line in text:
		try:
			line = line.split()
			mark = line[0]
			name = line[1:]
			name = " ".join(name)
			if int(mark) == high_mark:
				high_name = high_name + ", " + name
				more = more + 1
			if int(mark) > high_mark:
				high_mark = int(mark)
				high_name = name
		except ValueError:
			print('Invalid mark {} encountered. Skipping.'.format(mark))
			pass
	if more:
		print("Best student(s): {}\nBest mark: {}".format(high_name, high_mark))
	else:
		print("Best student: {}\nBest mark: {}".format(high_name, high_mark))
except FileNotFoundError:
	print('The file {:s} does not exist.'.format(f))